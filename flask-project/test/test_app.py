from application.models import Fighter, Roster, AddFighter, AddRoster
from flask_testing import TestCase
from flask import url_for
from application import app, db



class TestApp(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        db.create_all()
        tfighter1 = Fighter(name="jon jones", country="USA")
        troster1 = Roster(weight_class="light heavyweight", rank=1, fighter_name="jon jones")
        db.session.add(tfighter1)
        db.session.add(troster1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class TestHTML(TestApp):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_fighter(self):
        response = self.client.get(url_for('add_fighter'))
        self.assertEqual(response.status_code, 200)
      
    def test_view_fighter(self):
        response = self.client.get(url_for('view_fighter', fighter_name="jon jones"))
        self.assertEqual(response.status_code, 200)

    def test_update_fighter(self):
        response = self.client.get(url_for('update_fighter', name="jon jones"))
        self.assertEqual(response.status_code, 200)
        
    def test_add_fighter_to_roster(self):
        response = self.client.get(url_for('add_fighter_to_roster', fighter_name="jon jones"))
        self.assertEqual(response.status_code, 200)

    def test_view_roster(self):
        response = self.client.get(url_for('view_roster', fighter_name="jon jones"))
        self.assertEqual(response.status_code, 200)

    def test_update_roster(self):
        response = self.client.get(url_for('update_roster', id=1))
        self.assertEqual(response.status_code, 200)



class TestViewFighter(TestApp):
    def test_view_fighter(self):
        response = self.client.get(url_for('view_fighter'))
        assert 'jon jones'in response.data.decode()
        assert 'USA'in response.data.decode()


class TestDeleteFighter(TestApp):
    def test_delete_fighter(self):
        response = self.client.get(
            url_for('delete_fighter', name="jon jones"))
        self.assertEqual(response.status_code, 302)
        assert "view_fighter" in response.data.decode()

class TestAddFighterToRoster(TestApp):
    def test_add_fighter_to_roster(self):
        response = self.client.post(url_for('add_fighter_to_roster'), data=dict(weight_class="light heavyweight", rank=1, fighter_name="jon jones"), follow_redirects=True)
        assert 'view_roster'in response.data.decode()

class TestViewRoster(TestApp):
    def test_view_roster(self):
        response = self.client.get(url_for('view_roster'))
        assert 'light heavyweight'in response.data.decode()
        assert '1'in response.data.decode()
        assert 'jon jones'in response.data.decode()

class TestReleaseFighter(TestApp):
    def test_release_fighter(self):
        response = self.client.get(
            url_for('release_fighter', id=1))
        self.assertEqual(response.status_code, 302)
        assert "view_roster" in response.data.decode()
