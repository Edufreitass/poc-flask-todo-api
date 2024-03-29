from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """
                Método para converter um objeto usuário em um dicionário,
                útil para JSONificação de instâncias de usuário.
                """
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }
