import click
from logger import logger


@click.command()
@click.argument('rj_id', type=str)
@click.option('-s', '--star', type=int)
@click.option('-c', '--comment', type=str)
def review(rj_id: str, star: int, comment: str):
    logger.info(f'run command review with rj_id={rj_id}, star={star} comment={comment}')
    rj_id_int: int = int(rj_id[2:]) if rj_id.startswith('RJ') else int(rj_id)

    from asmrcli.core import create_database
    db = create_database()
    db.update_review(rj_id_int, star, comment)
    db.commit()



