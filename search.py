# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]
# Funcao de busca por profundidade
def depthFirstSearch(problem):
    # Inicializacao dos estados    
    start = problem.getStartState()
    c = problem.getStartState()
    exploredState = []
    exploredState.append(start)

    # Criando uma pilha para armazenagem dos estados
    states = util.Stack()
    stateTuple = (start, [])
    states.push(stateTuple)

    # Laco que verifica se os estados inicialmente sao vazios ou se ha algum
    # problema existente, se nao ele explora os estados seguintes.
    while not states.isEmpty() and not problem.isGoalState(c):
        state, actions = states.pop()
        exploredState.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if not coordinates in exploredState:
                c = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
    return actions + [direction]
    util.raiseNotDefined()
# Funcao de busca por extensao
def breadthFirstSearch(problem):
  print "Iniciando em:", problem.getStartState()
  
  # Variaveis para verificacao de se o objetivo foi ou nao alcancado
  reachedGoal=False
  exploredAll=False

  startState=problem.getStartState()
  
  # Tabela que armazena os estados ja explorados
  exploredStatesDictionary={}

  # Inserindo o estado inicial na primeira posicao da tabela
  exploredStatesDictionary[0] = problem.getStartState()

  # Tabela para armazenar as fronteiras
  frontierDictionary=util.Counter()

  # Lista de fronteiras, recebe os sucessores do problema sendo passado o estado inicial
  frontierList=problem.getSuccessors(problem.getStartState())
  vectorDictionary={} 
  
 
  # Pilha para armazenar os estados das fronteiras
  frontierQueue=util.Queue()
  
  # Lista que armazena acoes
  actionsQueue=[]
  
  # Lista que armazena os nos ja explorados
  addedNodes = []
  
  # Preenche a pilha com os estados de fronteiras
  for i in frontierList:
   fNode=i
   frontierQueue.push(fNode)
   addedNodes.append(fNode[0])
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    
    vectorDictionary[successor]=actionsThisFar
  
  seenAlready=1
  iteration =0 
  
  "===============================Inicializacao do loop principal===================================="
  while reachedGoal==False:
    
   iteration= iteration + 1
   
   for i in addedNodes:
     popped=addedNodes.pop()
     exploredStatesDictionary[seenAlready] = popped
     seenAlready = seenAlready + 1
     
   tempState=frontierQueue.pop()
   
   nextState=tempState[0]
   
   nextAction=tempState[1]
   # Salva o estado explorado
   
   reset = str(tempState[0])
   
   "Nova lista de acoes"
   newActionsList = vectorDictionary[reset]
   "Adiciona a proxima acao a ser executada"
   newActionsList.append(nextAction)
   
   "Seta a lista de acoes em execucao para a nova lista"
   actionsQueue=copy.deepcopy(newActionsList)
   
   currentState=nextState
  
   "=======================Verificacao do estado da meta a ser atingida============================"
   if (problem.isGoalState(currentState)):
    reachedGoal=True
	
   else:
    
    "Adiciona a nova fronteira de acordo com o estado atual"
    frontierList=problem.getSuccessors(currentState)
  
    for i in frontierList:
     explored=False
     counter = 0
 
     for k in exploredStatesDictionary:
      stateCo=exploredStatesDictionary[k]
  
      if ((i[0] == stateCo)): 
       explored = True
       counter = counter+1
       
      elif ((explored == False) and (k == ((len(exploredStatesDictionary))-1))):
       
       actionsThisFar=copy.deepcopy(actionsQueue)
       successor = str(i[0])
       
       vectorDictionary[successor]=actionsThisFar
       
       fNode = i
       
       frontierQueue.push(fNode)
      
       addedNodes.append(fNode[0])

  return actionsQueue
  
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  # Realiza inicialmente um busca pelo no com menor custo
  
  print "Iniciando em:", problem.getStartState()
  print "O inicio e o objetivo?", problem.isGoalState(problem.getStartState())
  print "Iniciar os sucessores:", problem.getSuccessors(problem.getStartState())
  
  # Variaveis para verificar se o objetivo foi ou nao atingido
  reachedGoal=False
  exploredAll=False
  previousCost = 0;
  
  startState=problem.getStartState()
  
  exploredStatesDictionary=util.Counter()
  exploredStatesDictionary[0] = problem.getStartState()
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState())

  # Vetor para listas de chaves
  vectorDictionary={}
  
  frontierQueue=util.PriorityQueue()
  
  actionsQueue=[]
  
  addedNodes=[]
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    vectorDictionary[successor]=actionsThisFar
   
  # Preenchimento da fila com os nos da fronteira
  for i in frontierList:
    fNode=i
    frontierQueue.push(fNode,i[2])
    addedNodes.append(fNode[0])
  
  seenAlready=1

  # Laco para explorar os estados
  while reachedGoal==False:
    for i in addedNodes:
      popped=addedNodes.pop()
      exploredStatesDictionary[seenAlready] = popped
      seenAlready = seenAlready + 1
   
    tempState=frontierQueue.pop()
    previousCost = tempState[2]
    nextState=tempState[0]
  
    nextAction=tempState[1]
    
    # Salva os estados ja explorados
    exploredStatesDictionary[seenAlready] = nextState
  
    seenAlready = seenAlready+1

    reset = str(tempState[0])

    newActionsList = vectorDictionary[reset]
    newActionsList.append(tempState[1])
   
  
    # Esvazia a lista de acoes antigas
    actionsQueue=copy.deepcopy(newActionsList)
   
    currentState=nextState
    
    # Checa se a meta ja foi atingida
    if (problem.isGoalState(currentState)):
      reachedGoal=True
	
    else:
      frontierList=problem.getSuccessors(currentState)
      for i in frontierList:
        explored=False
        counter=0
        for k in exploredStatesDictionary:
          stateCo=exploredStatesDictionary[k]
          
          if ((i[0] == stateCo)): 
           
            explored = True
            counter = counter+1
       
          elif ((explored == False) and (k == ((len(exploredStatesDictionary)))-1)):
              
            actionsThisFar=copy.deepcopy(actionsQueue)
            successor = str(i[0])
            vectorDictionary[successor]=actionsThisFar
            fNode = i
            newCost = i[2] + previousCost
            fNode=list(fNode)
            #update
            fNode[2]=newCost
            #back to tuple
            fNode=tuple(fNode)
            frontierQueue.push(fNode, newCost)
            addedNodes.append(fNode[0])
 
  length = len(actionsQueue)
  return actionsQueue
  
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  
  print "Iniciando em:", problem.getStartState()
  print "O inicio e o objetivo?", problem.isGoalState(problem.getStartState())
  print "Iniciar os sucessores:", problem.getSuccessors(problem.getStartState())
  
  reachedGoal=False
  exploredAll=False
  previousCost = 0;
  
  startState=problem.getStartState()
  
  exploredStatesDictionary=util.Counter()
  exploredStatesDictionary[0] = problem.getStartState()
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState())

  vectorDictionary={}
  
  frontierQueue=util.PriorityQueue()

  actionsQueue=[]
  
  addedNodes=[]
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    vectorDictionary[successor]=actionsThisFar
   
  # Preenche a pilha com os estados de fronteiras
  for i in frontierList:
    fNode=i
    frontierQueue.push(fNode,i[2])
    addedNodes.append(fNode[0])
  
  seenAlready=1
  while reachedGoal==False:
    for i in addedNodes:
     
      popped=addedNodes.pop()
      exploredStatesDictionary[seenAlready] = popped
      seenAlready = seenAlready + 1
  
    tempState=frontierQueue.pop()
    previousCost = tempState[2]
    nextState=tempState[0]
  
    nextAction=tempState[1]
    
    # Salva o estado explorado
    exploredStatesDictionary[seenAlready] = nextState
    
    seenAlready = seenAlready+1

    reset = str(tempState[0])

    newActionsList = vectorDictionary[reset]
    newActionsList.append(tempState[1])
   
    actionsQueue=copy.deepcopy(newActionsList)
   
    currentState=nextState

    if (problem.isGoalState(currentState)):
      reachedGoal=True
	
    else:
      frontierList=problem.getSuccessors(currentState)
      for i in frontierList:
        explored=False
        counter=0
        for k in exploredStatesDictionary:
          stateCo=exploredStatesDictionary[k]
         
          if ((i[0] == stateCo)): 
           
            explored = True
            counter = counter+1
       
          elif ((explored == False) and (k == ((len(exploredStatesDictionary)))-1)):
              
            actionsThisFar=copy.deepcopy(actionsQueue)
            successor = str(i[0])
            vectorDictionary[successor]=actionsThisFar
            fNode = i
            hCost=heuristic(i[0],problem)
            newCost = i[2] + previousCost + hCost
            fNode=list(fNode)
            
            fNode[2]=newCost
            
            fNode=tuple(fNode)
            frontierQueue.push(fNode, newCost)
            addedNodes.append(fNode[0])

  length = len(actionsQueue)
  return actionsQueue
  
  util.raiseNotDefined()
    
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch