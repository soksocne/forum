from rest_framework import serializers

from applications.comments.models import Comments
from applications.comments.serializers import CommentsSerializer
from applications.question.models import Question, Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title', 'image', 'problem')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        question = Question.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_rating = [i.rating for i in instance.comment.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating) / len(total_rating)
        else:
            rep['total_rating'] = 0
        rep['comment'] = CommentsSerializer(Comments.objects.filter(question=instance.id),
                                            many=True).data
        rep['like'] = instance.like.filter(like=True).count()
        return rep
