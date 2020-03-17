from sqlalchemy import or_


def base_query(model):
    """
    所有未被删除的记录
    """
    return model.query.filter(or_(model.is_delete.is_(None), model.is_delete == 0))


