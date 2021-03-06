from rest_framework import serializers
from .models import ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ('id', 'title', 'date', 'review', 'private', 'user', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')

    
    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.user.pk: # guarantees current user can only update their own info
                raise serializers.ValidationError({"authorize": "You do not have permission to do that."})

        if 'title' in validated_data:
            instance.title = validated_data['title']
        if 'date' in validated_data:
            instance.date = validated_data['date']
        if 'review' in validated_data:
            instance.review = validated_data['review']
        if 'private' in validated_data:
            instance.private = validated_data['private']

        instance.save()

        return instance


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ('id', 'title', 'date', 'review', 'private', 'user', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')