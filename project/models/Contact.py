from extentions import *



class Contact(db.Model):
    __tablename__="contacts"
    user_id=db.Column(db.Integer)
    phone=db.Column(db.String(11),nullable=True)
    city=db.Column(db.String(50),nullable=True)
    user=db.relationship("User",back_populates="contact")


    __table_args__=(
        db.PrimaryKeyConstraint("user_id",name="pk_id"),
        db.ForeignKeyConstraint(["user_id"],["users.id"],onupdate="CASCADE",ondelete="CASCADE"),
        db.Index("index1","phone",'city')
        )