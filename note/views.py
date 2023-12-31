from .models import *
from .serializer import *
import pyttsx3, uuid, os
from datetime import date
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from django.contrib.auth.models import User

#views 
class NotesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk=None):
        try:
            return Audio_note.objects.get(pk=pk)
        except Audio_note.DoesNotExist:
            raise Http404 
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None, format=None):

        user = self.request.query_params.get('user')
        if user is not None:
            note = Audio_note.objects.all()
            queryset = note.filter(user_id=user)
            serializer = NoteSerializer(queryset, many=True)
            return Response(serializer.data)
        
        if not pk:
            note = Audio_note.objects.all()
            serializer = NoteSerializer(note, many=True)
            return Response(serializer.data)

        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

        
        # return Response({})
    permission_classes = [IsAuthenticated]
    def post(self, request, method=None):
        title = request.data.get('title')
        note = request.data.get('note')
        voice = request.data.get('voice')
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        print(user)
        engine = pyttsx3.init()
        # convert this text to speech
        voices = engine.getProperty("voices")
        if voice == 'female':
            engine.setProperty('voice', voices[0].id)
        elif voice == 'male':
            engine.setProperty('voice', voices[1].id)
        
        file_name = uuid.uuid4().hex+"_file.wav"
        engine.save_to_file(note, f'media/audios/{file_name}')
        engine.runAndWait()
   
        audio_note = Audio_note.objects.create(
            title= title,
            note= note,
            audio_file = 'media/audios/'+file_name,
            user = user
        )
        audio_note.save()
        return Response({"type":"success", "message":"Note successfully saved!"})
class NoteDeleteAPI(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        try:
            instance = Audio_note.objects.get(pk=pk)
        except Audio_note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        file = instance.audio_file
        if os.path.isfile(file):
            os.remove(file)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
