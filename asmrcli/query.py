import click
from asmrcli.core import create_database


@click.group()
def query():
    return


@click.command()
def web():
    """Not implemented"""
    raise NotImplementedError


@click.command()
@click.argument('keyword', type=str)
def local(keyword: str):
    """
    supports some simple queries,
    it will match the input with name, circle_name and tag field.
    if you want to use more complex queries, please use asmr sql instead.
    """
    from database.database import ASMR, ASMRs2Tags, Tag
    from common.output import print_table

    db = create_database()
    res = (
        db.query(
            ASMR.id,
            ASMR.title,
            ASMR.circle_name,
            ASMR.nsfw,
            ASMR.has_subtitle,
            ASMR.count,
            ASMR.star,
        )
        .join(ASMRs2Tags, ASMRs2Tags.asmr_id == ASMR.id)
        .join(Tag, Tag.id == ASMRs2Tags.tag_id)
        .filter(
            ASMR.circle_name.contains(keyword)
            | ASMR.title.contains(keyword)
            | Tag.name.contains(keyword)
        )
        .group_by(ASMR.id)
        .all()
    )

    print(res)
    print_table(
        titles=[
            'id',
            'title',
            'circle_name',
            'nsfw',
            'subtitle',
            'count',
            'star',
        ],
        rows=res,
    )


query.add_command(local)
