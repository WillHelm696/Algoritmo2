import math

class AVLTree:
     root = None

class AVLNode:
	parent = None
	leftnode = None
	rightnode = None
	key = None
	value = None
	count = None
	height = None
	bf = None
'------------------------------------------------------------'
def search(B,element):
	if B.root!=None:
		return Búsqueda(B.root,element)
	return None
def Búsqueda(Current,element):
	if Current!=None:
		if Current.value==element:
			return Current.key
		key=Búsqueda(Current.leftnode,element)
		if key==None:
			key=Búsqueda(Current.rightnode,element)
		return key
'------------------------------------------------------------'
def access(B,key):
	if B.root!=None:
		return Acceso(B.root,key)
	return None
def Acceso(Current,key):
	if Current!=None:
		if Current.key==key:
			return Current.value
		elif key<Current.key:
			return Acceso(Current.leftnode,key)
		elif Current.key<key:
			return Acceso(Current.rightnode,key)
	return None
'------------------------------------------------------------'
def update(B,element,key):
	if B.root!=None:
		return Actualizar(B.root,element,key)
	return None
def Actualizar(Current,element,key):
	if Current!=None:
		if Current.key==key:
			Current.value=element
			return Current.key
		elif key<Current.key:
			return Actualizar(Current.leftnode,element,key)
		elif Current.key<key:
			return Actualizar(Current.rightnode,element,key)
	return None
'------------------------------------------------------------'
def haltura(avlnode):
    if avlnode is not None:
        left_height = haltura(avlnode.leftnode)
        right_height = haltura(avlnode.rightnode)
        # La altura del árbol es la altura máxima de sus subárboles más 1
        return max(left_height, right_height) + 1
    return 0

def height(avlnode):
	if avlnode !=None:
		if avlnode.bf > 0:
			height(avlnode.leftnode)
		else :
			height(avlnode.rightnode)
		return avlnode.height
#////////////////////////////////////////////////////////////////////////
def rotateLeft(Tree,avlnode):
    new_root = avlnode.rightnode
    avlnode.right = new_root.leftnode
    if new_root.leftnode:
        new_root.leftnode.parent = node
    new_root.parent = avlnode.parent
    if not avlnode.parent:
        root = new_root
    elif avlnode == avlnode.parent.leftnode:
        avlnode.parent.leftnode = new_root
    else:
        avlnode.parent.rightnode = new_root
    new_root.leftnode = avlnode
    avlnode.parent = new_root
    #node.height = max(height(node.leftnode), height(node.rightnode)) + 1
    #new_root.height = max(height(new_root.leftnode), height(new_root.rightnode)) + 1
    return new_root
        
def rotateRight(Tree,avlnode):
    new_root = avlnode.leftnode
    avlnode.leftnode = new_root.rightnode
    if new_root.rightnode:
        new_root.rightnode.parent = avlnode
    new_root.parent = avlnode.parent
    if not avlnode.parent:
        root = new_root
    elif avlnode == avlnode.parent.rightnode:
        avlnode.parent.rightnode = new_root
    else:
        avlnode.parent.leftnode = new_root
    new_root.rightnode = avlnode
    avlnode.parent = new_root
    #node.height = max(height(node.leftnode),height(node.rightnode)) + 1
    #new_root.height = max(height(new_root.left),height(new_root.rightnode)) + 1
    return new_root
#////////////////////////////////////////////////////////////////////////
def calculateBalance(AVLTree): 
    if AVLTree.root!=None:
        calculate_bf(AVLTree.root)
    return AVLTree

def calculate_bf(avlnode):
    if avlnode !=None:
        if avlnode.leftnode == avlnode.rightnode :
            avlnode.bf = 0
        avlnode.bf = haltura(avlnode.leftnode) - haltura(avlnode.rightnode)
        calculate_bf(avlnode.leftnode)
        calculate_bf(avlnode.rightnode)
#////////////////////////////////////////////////////////////////////////
def reBalance(AVLTree):
    if AVLTree.root!=None:
        recalculate_fb(AVLTree.root)
    return AVLTree

def recalculate_fb(avlnode):
	if avlnode !=None:
		recalculate_fb(avlnode.leftnode)
		recalculate_fb(avlnode.rightnode)
	if avlnode.leftnode == avlnode.rightnode :
		avlnode.bf = 0
	else:
		#avlnode.bf = height(avlnode.leftnode) - height(avlnode.rightnode)
		avlnode.bf = haltura(avlnode.leftnode) - haltura(avlnode.rightnode)
		if avlnode.bf > 1 :
			if avlnode.rightnode==None:
				if avlnode.leftnode.bf<0:
					rotateRight(avlnode.leftnode)			
			new_root = rotateRight(avlnode)
			recalculate_fb(new_root)
		elif avlnode.bf < -1 :
			if avlnode.leftnode==None:
				if avlnode.rightnode.bf>0:
					rotateRight(avlnode.rightnode)
			new_root = rotateLeft(avlnode)
			recalculate_fb(new_root)
#////////////////////////////////////////////////////////////////////////
def insert(B,element,key):
	avlnode=AVLNode()
	avlnode.key=key
	avlnode.value=element
	avlnode.bf=0
	avlnode.height = 0
	avlnode.count=0
	if B.root==None:
			B.root=avlnode
			return key
	Node = Add_Node(B.root,avlnode)
	return Node.key

def Add_Node(Current,avlnode):
	if Current.key > avlnode.key:
		if Current.leftnode==None:
			Current.leftnode=avlnode
			avlnode.parent=Current
			update_bf(avlnode)
		else:
			Current.count +=1
			Node = Add_Node(Current.leftnode,avlnode)
			#Current.height = max(Current.leftnode.height,Current.rightnode.height)+1
			return Node
	elif Current.key<avlnode.key :
		if Current.rightnode==None:
			Current.rightnode=avlnode
			avlnode.parent=Current
			update_bf(avlnode)
		else:
			Current.count +=1
			Node = Add_Node(Current.rightnode,avlnode)
			#Current.height = max(Current.leftnode.height,Current.rightnode.height)+1
			return Node
	avlnode.parent=Current
	return avlnode

def update_bf(avlnode):
	if avlnode !=None:
		if avlnode.leftnode == None and avlnode.rightnode == None:
			avlnode.bf = 0
		else:
			avlnode.bf = haltura(avlnode.leftnode) - haltura(avlnode.rightnode)
			if avlnode.bf > 1 :
				print("Entra R")
				new_node=rotateRight(avlnode)
				update_bf(new_node.rightnode)
			elif avlnode.bf < -1:
				print("Entra L")
				new_node = rotateLeft(avlnode)
				update_bf(new_node.leftnode)
		update_bf(avlnode.parent)
		
#////////////////////////////////////////////////////////////////////////
def delete(B,element):
	key=search(B,element)
	if key!=None:
		return deleteKey(B,key)
	return None

def deleteKey(B,key):
	if access(B,key)!=None:
		avlnode=Node_Raiz(B,key)
		update_bf(avlnode.parent)
		return avlnode.key
	return None
'------------------------------------------------------------'
def Node_Raiz(B,key):
	if B.root.key==key:
		Node=B.root
		if Node.leftnode!=None or Node.rightnode!=None:
			B.root=Node_Interno(B.root,key)
		else:
			B.root=Node.leftnode 
		return Node
	return Node_Interno(B.root,key) 

def Node_Hoja(Node,key):
	Rama=Node.parent 
	if Rama.leftnode!=None:
		if Rama.leftnode.key==key:
			Rama.leftnode=Node.leftnode
	if Rama.rightnode!=None:
		if Rama.rightnode.key==key:
			Rama.rightnode=Node.rightnode
	Rama.height = max(Rama.leftnode.height,Rama.rightnode.height)
	return Node
	
def Node_Interno(Current,key):
	if Current!=None:
		if Current.key==key:
			Rama=Current
			Node=Current
			if Rama.leftnode==None and Rama.rightnode==None:
				return Node_Hoja(Current,key)
			elif Rama.leftnode!=None:
				Current=Current.leftnode
				while Current.rightnode!=None:
					Current=Current.rightnode
					Current.count -= 1					
			elif Rama.rightnode!=None:
				Current=Current.rightnode
				while Current.leftnode!=None:
					Current=Current.leftnode
					Current.count -= 1
			elif Current.rightnode!=None or Current.leftnode!=None:
				return Node_Interno(Current,Current.key)
			Hoja=Node_Hoja(Current,Current.key)
			Hoja.rightnode=Rama.rightnode
			Hoja.leftnode=Rama.leftnode
			Hoja.parent=Rama.parent
			if Rama.parent==None:
				return Hoja
			#--------------------	
			else:
				Rama=Hoja
			#--------------------					
		elif key<Current.key:
			Current.count -= 1
			Node = Node_Interno(Current.leftnode,key)
			Current.height = max(Current.leftnode.height,Current.rightnode.height)
		elif Current.key<key:
			Current.count -= 1
			Node = Node_Interno(Current.rightnode,key)
			Current.height = max(Current.leftnode.height,Current.rightnode.height)
	return Node
