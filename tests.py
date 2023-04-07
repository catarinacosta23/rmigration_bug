from django.test import TestCase
from rmigrate.models import User, A, B

class TestModels(TestCase):

    def test_bug_fix(self):
        # create a user and A object
        user = User.objects.create_user(username='testuser', password='testpass')
        a = A.objects.create(user=user)

        # create a B object associated with the A object
        b = B.objects.create(a=a)

        # delete the B object first
        b.delete()

        # now try to delete the A object again
        a.delete()

        # check that the A object was successfully deleted
        self.assertFalse(A.objects.filter(id=a.id).exists(), "Erro ao excluir objeto A após criar objeto B associado a ele.")
