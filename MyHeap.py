"""
    Implementatie van een Linked Based Heap
"""
class heapItem:
    def __init__(self, key):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een heapItemType, dit is het type van de elementen
            in de heap. Een element van dit type heeft een zoeksleutel
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Een heapItem is aangemaakt
        -------------------------------------------------------
        """
        self.left = None
        self.right = None
        self.key = key
        self.parent = None


class Heap:
    def __init__(self,maxHeap=True):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege min-/ max-heap a.d.h.v. te opgegeven
            :param maxHeap
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Er is een heap aangemaakt
        -------------------------------------------------------
        """
        self.root = None
        self.size = 0
        self.maxHeap = maxHeap

    def heapIsEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een heap leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de BST leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.size == 0:
            return True
        else:
            return False

    def heapInsert(self, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Voegt newItem toe aan eenheap met items met unieke zoeksleutels
            verschillend van de zoeksleutel van newItem
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een heap aangemaakt zijn
        Postconditions:
            Het newItem wordt aan de heap toegevoegd, gesorteerd
            volgens het type van de heap.
        -------------------------------------------------------
        Return : True geeft weer dat het toevoegen gelukt is anders False
        -------------------------------------------------------
        """
        # Maakt een niewe heap item
        newHeapItem = heapItem(newItem)
        # Kijkt of de heap leeg is, kon ook a.d.h.v de size of de isEmpty methode
        if self.root is None:
            # Zet de root gelijk aan het newItem
            self.root = newHeapItem
            # Verhoog de size van de heap
            self.size += 1
            return True
        last_node = self.getLastNode()

        # Kijkt of zowel de linker als rechter deelbomen van de root bezet zijn
        #if self.root.left is not None and self.root.right is not None:
        if last_node.left is None:
            last_node.left = newHeapItem
        else:
            last_node.right = newHeapItem
        newHeapItem.parent = last_node
        # Anders kijk je welke nog niet bezet is
        #else:
            #if self.root.left is None:
            #    self.root.left = newHeapItem
            #else:
            #    self.root.right = newHeapItem
            #newHeapItem.parent = self.root

        self.size += 1
        self.trickleUp(newHeapItem)
        self.rearangeHeap()
        return True

    def heapDelete(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijderd rootItem uit de heap
            Het element met de grootste zoeksleutel (bij een max-heap) of
            het element met de kleinste zoeksleutel (bij een min-heap)
            wordt verwijderd.
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een heap aangemaakt zijn
        Postconditions:
            Het root wordt uit de heap verwijderd, afhankelijk van max of min heap
        -------------------------------------------------------
        Return : True geeft weer dat het verwijderen gelukt is anders False
        -------------------------------------------------------
        """
        # Kijkt of de heap leeg is, kon ook a.d.h.v de size of de isEmpty methode
        if self.root is None:
            return (None, False)
        else:
            # Indien de heap niet leeg is dan slagen we de root key op in rootItem
            rootItem = self.root.key
            # Zoek de laatste Knoop
            last_node = self.getLastNode()
            # Kijkt of de laatste knoop niet gelijk is aan de root
            if last_node is not self.root:
                # Zet de waarde van de laatste knoop in de root
                self.root.key = last_node.key
                # Slaag de ouder van de laatste knoop op in een variable parent
                parent = last_node.parent
                if parent is not None:
                    # Kijkt of de laatste knoop in het linker kind zit
                    if parent.left == last_node:
                        # Maak linker kind leeg
                        parent.left = None
                    # Kijkt of de laatste knoop in het recter kind zit
                    elif parent.right == last_node:
                        # Maak linker kind leeg
                        parent.right = None
                # Decrement size
                self.size -= 1
                # Als er niet aan de bovenstaande condities wordt voldaan doen we een trickleDown
                self.trickleDown(self.root)
            else:
                # Indien de laatste knoop wel gelijk is aan de knoop dan verwijderen we de root (in het geval size == 1)
                self.root = None
                # Decrement size
                self.size -= 1
            self.rearangeHeap()
            return (rootItem, True)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode stelt een heap voor als een dict.
        -------------------------------------------------------
        Preconditite:
            De heap mag niet leeg zijn
        Postconditions:
            De waarden van de zoeksleutels worden weergegeven in een dict.
        -------------------------------------------------------
        """
        def save_heap(heapItem):
            data = {}
            if heapItem is None:
                return None
            data['root'] = heapItem.key
            if heapItem.left is not None or heapItem.right is not None:
                data['children'] = []
                if heapItem.left is not None:
                    data['children'].append(save_heap(heapItem.left))
                else:
                    data['children'].append(None)
                if heapItem.right is not None:
                    data['children'].append(save_heap(heapItem.right))
                else:
                    data['children'].append(None)
            return data
        return save_heap(self.root)

    def load(self, data):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode laad een dict. in als een heap
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De dict. wordt ingeladen als een heap, met voor elke heapItem
            de key gelijk aan de val van de 'root' key
        -------------------------------------------------------
        """
        def load_bst(dict, parent):
            # Checkt of de dict niet leeg is
            if dict is None:
               return None
            # Maakt een knoop aan voor de root, met als key de value die de root key heeft
            node = heapItem(dict['root'])
            node.parent = parent
            self.size += 1
            # Kijk of er kinderen zijn
            if 'children' in dict:
                # Kijkt op linker kinderen
                if dict['children'][0] is not None:
                    node.left = load_bst(dict['children'][0], node)
                else:
                    None
                # Kijkt op rechter kinderen
                if len(dict['children']) > 1 and dict['children'][1] is not None:
                    node.right = load_bst(dict['children'][1], node)
                else:
                    None
            return node
        self.size = 0
        # Zet de ingeladen BST gelijk aan onze self.root
        self.root = load_bst(data, None)

    """
    -------------------------------------------------------
    Beschrijving:
        Alle helpfuncties die worden gebruikt voor het 
        bewerkingscontract te kunnen nakom.
    -------------------------------------------------------
    """
    def trickleUp(self, node):
        # Implementatie voor max-heap
        if self.maxHeap == True:
            parent = node.parent
            while parent is not None and node.key > parent.key:
                node.key, parent.key = parent.key, node.key
                node = parent
                parent = node.parent
        # Implementatie voor min-heap
        else:
            parent = node.parent
            while parent is not None and node.key < parent.key:
                node.key, parent.key = parent.key, node.key
                node = parent
                parent = node.parent

    def trickleDown(self, node):
        # Implementatie voor max-heap
        if self.maxHeap == True:
            # Get the left and right children of the node
            leftChild = node.left
            rightChild = node.right
            # Find the largest among node, left child and right child
            largest = node
            if leftChild is not None and leftChild.key > largest.key:
                largest = leftChild
            if rightChild is not None and rightChild.key > largest.key:
                largest = rightChild
            # If node is not the largest, swap the node with the largest and recursively trickle down the largest node
            if largest != node and self.size > 3 and largest is not None:
                node.key, largest.key = largest.key, node.key
                self.trickleDown(largest)
            if self.root.left is not None:
                if self.root.key < self.root.left.key:
                    temp = self.root.key
                    self.root.key = leftChild.key
                    leftChild.key = temp
                    self.root.left.parent = self.root
                    self.root.parent = None
            if self.root.right is not None:
                if self.root.key < self.root.right.key:
                    temp = self.root.key
                    self.root.key = rightChild.key
                    rightChild.key = temp
                    self.root.right.parent = self.root
                    self.root.parent = None
        # Implementatie voor min-heap
        else:
            left_child = node.left
            right_child = node.right
            if left_child is None:
                return
            smallest_child = left_child
            if right_child is not None and right_child.key < left_child.key:
                smallest_child = right_child
            if smallest_child.key < node.key:
                node.key, smallest_child.key = smallest_child.key, node.key
                self.trickleDown(smallest_child)

    def getMaxChild(self, node):
        if node.left is None or node.right is None:
            if node.left is None:
                return node.right
            elif not node.right:
                return node.left
        else:
            return node.left if node.left.key > node.right.key else node.right

    def getMinChild(self, node):
        if not node.left:
            return None
        elif not node.right:
            return node.left
        else:
            return node.left if node.left.key < node.right.key else node.right

    def getLastNode(self):
        if self.root is None:
            return None
        if self.root.left is None or self.root.right is None:
            node = self.root
        else:
            height = 0
            node = self.root
            while node.left is not None:
                height += 1
                node = node.left
            last_index = (2 ** (height + 1)) - 2
            node = self.getNode(last_index)

        return node

    def getNode(self, index):
        height = 0
        node = self.root
        while node.left is not None:
            height += 1
            node = node.left
        current = self.root
        for i in range(height):
            if (index + 1) % 2 == 0:
                current = current.right
            else:
                current = current.left
            index = (index - 1) // 2
        return current

    def rearangeHeap(self):
        node = self.root
        leftChild = node.left
        rightChild = node.right
        if leftChild is None and rightChild is not None:
            node.left = rightChild
            node.right = leftChild
        elif leftChild is not None and rightChild is not None and leftChild.left is not None and leftChild.left.left is not None and leftChild.left.right is None:
            leftChild.right = leftChild.left
            leftChild.left = leftChild.left.left
            leftChild.left.left = None
            leftChild.right.left = None
        elif leftChild.left is None and leftChild.right is not None:
            leftChild.left = leftChild.right
            leftChild.right = None
        if leftChild is not None:
            if leftChild.left is not None and leftChild.right is not None:
                if leftChild.left.key == leftChild.right.key:
                    leftChild.right = None





if __name__ == "__main__":
    t = Heap()
    print(t.heapIsEmpty())
    print(t.heapDelete()[1])
    print(t.heapInsert(5))
    print(t.heapInsert(8))
    print(t.heapIsEmpty())
    print(t.save())
    t.load({'root': 10, 'children': [{'root': 5}, None]})
    t.heapInsert(15)
    print(t.save())
    result = t.heapDelete()
    print(result[0])
    print(result[1])
    print(t.save())
    """# Vraag 3
    t = Heap()
    t.heapInsert(2)
    t.heapInsert(3)
    t.heapInsert(1)
    print(t.save())
    t.heapInsert(5)
    print(t.save())
    t.heapInsert(9)
    print(t.save())"""
    """# Vraag 4
    t = Heap()
    t.load({'root': 9, 'children': [{'root': 5, 'children': [{'root': 2}, {'root': 3}]}, {'root': 1}]})
    result = t.heapDelete()
    print(t.save())
    result = t.heapDelete()
    print(t.save())"""
    """# Vraag 5
    t = Heap()
    t.load({'root': 3, 'children': [{'root': 2}, {'root': 1}]})
    t.heapInsert(5)
    t.heapInsert(4)
    result = t.heapDelete()
    print(t.save())"""
    """t = Heap()
    t.heapInsert(2)
    t.heapInsert(3)
    t.heapInsert(5)
    t.heapInsert(6)
    t.heapInsert(9)
    t.heapInsert(10)
    print(t.save())
    t.heapDelete()
    print(t.save())"""