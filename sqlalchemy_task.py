
/

def retrieve_item(db: SessionLocal, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db: SessionLocal, item_id: int, updated_data: ItemPydantic):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        for key, value in updated_data.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    return None

def delete_item(db: SessionLocal, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return db_item