from sqlalchemy import select, func
from extentions import db
from sqlalchemy.ext.hybrid import hybrid_property
from models.Task import Task

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    contact = db.relationship("Contact", back_populates="user", uselist=False)
    tasks = db.relationship("Task", back_populates="user")

    __table_args__ = (
        db.PrimaryKeyConstraint("id", name="pk_id"),
        db.UniqueConstraint("user_name", name="uniqu"),
        db.Index('index1', "user_name", "password")
    )

    @hybrid_property
    def tasks_count(self):
        return len(self.tasks)

    @tasks_count.expression
    def tasks_count(cls):
        return (
            select(func.count(Task.id))
            .where(Task.user_id == cls.id)
            .correlate(cls)
            .scalar_subquery()
        )