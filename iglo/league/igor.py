from rest_framework import serializers
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.renderers import JSONRenderer
from rest_framework_extensions.routers import ExtendedDefaultRouter

from django.conf import settings
from league.models import Game, WinType, Player

import accurating
import json

class IgorMatchSerializer(ModelSerializer):
    p1 = serializers.CharField(source="black.player.nick")
    p2 = serializers.CharField(source="white.player.nick")
    season = serializers.IntegerField(source="group.season.number")
    winner = serializers.CharField(source="winner.player.nick")

    class Meta:
        model = Game
        fields = [
            "p1",
            "p2",
            "winner",
            "season",
        ]

def igor_matches():
    return (
        Game.objects.all()
        .filter(win_type__in=[WinType.POINTS, WinType.RESIGN, WinType.TIME])
        .exclude(winner=None)
        .select_related("black__player", "white__player", "group__season", "winner__player")
    )

class IgorViewSet(ListModelMixin, RetrieveModelMixin, NestedViewSetMixin, GenericViewSet):
    queryset = igor_matches()
    serializer_class = IgorMatchSerializer
    pagination_class = None


def register(router: ExtendedDefaultRouter):
    router.register("igor-matches", IgorViewSet, basename="api-igor-matches")


def recalculate_igor():

    ar_config = accurating.Config(**settings.IGOR_CONFIG)

    matches = [
        dict(
            p1=game.black.player.nick,
            p2=game.white.player.nick,
            season=game.group.season.number,
            winner=game.winner.player.nick,
        ) for game in igor_matches()
    ]
    # The above code is equivalent to:
    # matches_json = JSONRenderer().render(IgorMatchSerializer(igor_matches(), many=True).data)
    # matches = json.loads(matches_json)
    ar_data = accurating.data_from_dicts(matches)
    model = accurating.fit(ar_data, ar_config)

    ratings = {}
    for nick, season_ratings in model.rating.items():
        last_season = max(season_ratings.keys())
        ratings[nick] = season_ratings[last_season]
    to_update = Player.objects.filter(nick__in=model.rating.keys())
    for obj in to_update:
        if obj.nick in ratings:
            obj.igor = ratings[obj.nick]
    Player.objects.bulk_update(to_update, fields=['igor'])
