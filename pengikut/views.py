from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
#from rest_framework import permission

from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import Statevector
from numpy import sqrt


from qiskit.providers.basic_provider import BasicProvider
 


from pengikut.models import Pengikut
from pengikut.serializers import PengikutSerializers
# Create your views here.

class PengikutApiView(APIView):

    def get(self, request):
        pengikut = Pengikut.objects.all()
        serial = PengikutSerializers(pengikut, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'nama_asli': request.data.get('nama_asli'), 
            'nama_samaran': request.data.get('nama_samaran'), 
        }
        serializer = PengikutSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KuantumAPI(APIView):

    def get(self, request):

        # Hypotetical quantum circuit

        q = QuantumCircuit(1)
        q.x(0)
        q.h(0)
        p = q.measure_all()
        

        simulator = BasicProvider().get_backend('basic_simulator')
        job = simulator.run(q, shots=100)
        # Return counts
        counts = job.result().get_counts(q) # hasil dekripsi baru dimasukkan kedalam Database
        print(counts)
        return Response(counts, status=status.HTTP_200_OK)