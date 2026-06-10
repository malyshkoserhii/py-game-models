import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "r") as players_file:
        data = json.load(players_file)

    for player_name, player_info in data.items():
        race = player_info["race"]

        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        for skill in race.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )

        guild_obj = None
        guild = player_info.get("guild")

        if guild:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild.get("description")
            )

        Player.objects.get_or_create(
            nickname=player_name,
            race=race_obj,
            guild=guild_obj,
            bio=player_info.get("bio"),
            email=player_info.get("email")
        )


if __name__ == "__main__":
    main()
