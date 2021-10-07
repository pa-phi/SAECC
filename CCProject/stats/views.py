from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers as s

# Returns Team Data
@api_view(['GET'])
def getTeams(request):
  teams = models.Team.objects.all()
  serializer = s.TeamSerializer(teams, many=True)
  return Response(serializer.data)

# Returns Match Data
@api_view(['GET'])
def getMatches(request):
  matches = models.Match.objects.all()
  serializer = s.MatchSerializer(matches, many=True)
  return Response(serializer.data)

# Returns Player Data
@api_view(['GET'])
def getPlayers(request):
  players = models.Player.objects.all()
  serializer = s.PlayerSerializer(players, many=True)
  return Response(serializer.data)

# Update Match Data
@api_view(['UPDATE'])
def updateMatch(request):
  data = request.data
  store = Store.objects.create(
    name = data['name'],
    location = data['location'],
    phone = data['phone'],
    website = data['website'],
    hoursOfOperation = data['hoursOfOperation'],
    category = data['category'],
  )
  serializer = StoreSerializer(store, many=False)
  return Response(serializer.data)

@api_view(['DELETE'])
def deleteStore(request, pk):
  store = Store.objects.get(id=pk)
  store.delete()
  return Response('Store was deleted!')

# Returns information about the API endpoints
@api_view(['GET'])
def getRoutes(request):
  routes = [
    {
      'Endpoint': '\teams',
      'method': 'GET',
      'body': None,
      'description': 'Returns all teams'
    },
    {
      'Endpoint': '\matches',
      'method': 'GET',
      'body': None,
      'description': 'Returns current match data'
    },
    {
      'Endpoint': '\live\<int:id>',
      'method': 'UPDATE',
      'body': {
        'shots': []
      },
      'description': 'Updates match with corresponding id'
    },
  ]
  return Response(routes)