from rest_framework import serializers

from applications.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title', 'image', 'problem')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        question = Question.objects.create(**validated_data)
        return question
