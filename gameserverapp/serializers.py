from .models import Board,Game, Player
from rest_framework import serializers



class BoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		exclude = ('placed_words',)



class GameSerializer(serializers.ModelSerializer):
	
	#serializing the relations
	admin_player = serializers.StringRelatedField()
	current_player = serializers.StringRelatedField()
	players = serializers.StringRelatedField(many=True)
	game_status = serializers.SerializerMethodField()
	
	class Meta:
		model = Game
		exclude = ('players','min_players','max_players')

	def get_game_status(self,obj):
		return obj.get_game_status_display()	


class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = '__all__'


