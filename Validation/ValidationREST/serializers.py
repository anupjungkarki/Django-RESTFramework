from rest_framework import serializers
from .models import Student

# Use of Validators
def start_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name Must Start With a!!')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=114, validators=[start_with_a])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # For Deserialization
    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    # Below Section is the validation section using (Fields Level Validation)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat is Already Full!!')
        return value

    # Below Section is the validation section using (ObjectLevel Validation)
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower == 'solu':
    #         raise serializers.ValidationError('City Must Be Solu')
    #     return data
    #


