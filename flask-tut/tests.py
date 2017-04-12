import unittest
from models import User

from flask_proj import app, db

class AppTestCase(unittest.TestCase):

    def SetUp(self):
        app.config['Testing'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///app.db'
        db.create_all()

    def TearDown(self):
        db.drop_all()

    def test_hello(self):
        expected = "Hello World"
        self.assertEqual(expected, "Hello World")

    def test_app_config(self):
        self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'],
                                    'sqllite:///app.db')

    def test_user_model(self):
        u = User(username='john', email='john@email.com')
        db.session.add(u)
        db.session.commit()

        users = User.query.all()
        self.assertEqual(len(users),1)
