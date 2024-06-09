from rest_framework import serializers
from pengikut.models import Pengikut

class PengikutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pengikut
        fields = ['id', 'nama_asli', 'nama_samaran']