"""
    Implementatie van een 2-3-4 boom.
"""

class treeItem:
    def __init__(self, keys=[], vals=[]):
        """
        -------------------------------------------------------
        Beschrijving:
            Initialiseert elke item/knoop van de boom, met zoeksleutels en waarden
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Een item/knoop van de boom is aangemaakt
        -------------------------------------------------------
        """
        self.keys = keys
        self.vals = vals
        self.children = []

    def isLeaf(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een knoop/treeItem een blad is
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Er wordt een boleaanse terug gegeven indien de knoop
            een blad is
        -------------------------------------------------------
        """
        if len(self.children) == 0:
            return True
        else:
            return False

def createTreeItem(key,val):
    """
    -------------------------------------------------------
    Beschrijving:
        Creëert een TreeItemType, dit is het type van de elementen in de 2-3-4.
    -------------------------------------------------------
    Preconditie:
        /
    Postconditie:
        Een lege treeItem is aangemaakt
    -------------------------------------------------------
    """
    return treeItem(key, val)

class TwoThreeFourTree:
    def __init__(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege 2-3-4 boom
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Er is een 2-3-4 boom aangemaakt
        -------------------------------------------------------
        """
        self.root = None

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een 2-3-4 boom leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de 2-3-4 boom leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.root is None:
            return True
        else:
            return False

    def search(self, searchKey):
        """
        -------------------------------------------------------
        Beschrijving:
            Zoekt in de 2-3-4 boom naar het item met searchKey als zoeksleutel
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De knoop wodt teruggeven
        -------------------------------------------------------
        """
        node = self.root
        while node is not None:
            # Check if the key is in the node
            if searchKey in node.keys:
                return node
            # Check if there are children and choose the correct path
            elif node.children:
                if searchKey < node.keys[0]:
                    node = node.children[0]
                elif len(node.keys) == 2 and searchKey > node.keys[1]:
                    node = node.children[2]
                elif searchKey > node.keys[0] and searchKey < node.keys[1]:
                    node = node.children[1]
                else:
                    return None
            else:
                return None
        return None

    def insertItem(self, newItem):
        new_key = newItem.keys
        if not self.root:
            self.root = treeItem([newItem.keys], [newItem.vals])
            return

        current_node = self.root
        while not current_node.isLeaf:
            for i in range(len(current_node.keys)):
                if new_key < current_node.keys[i]:
                    current_node = current_node.children[i]
                    break
                elif i == len(current_node.keys) - 1:
                    current_node = current_node.children[-1]

        index = 0
        while index < len(current_node.keys) and new_key > current_node.keys[index]:
            index += 1
        current_node.keys.insert(index, new_key)
        current_node.vals.insert(index, newItem.vals)

        if len(current_node.keys) > 3:
            self.split_node(current_node)

    def split_node(self, node):
        # Kijkt eerst of de lengte even of oneven is - Als er twee si- blings een item kunnen uitlenen, kies je voor de linkse.
        if (len(node.keys) % 2 == 0):
            middle_index = (len(node.keys) // 2)-1
        else:
            middle_index = len(node.keys) // 2
        middle_key = node.keys[middle_index]
        middle_val = node.vals[middle_index]
        left_keys = node.keys[:middle_index]
        left_vals = node.vals[:middle_index]
        right_keys = node.keys[middle_index + 1:]
        right_vals = node.vals[middle_index + 1:]
        left_node = treeItem(left_keys, left_vals)
        right_node = treeItem(right_keys, right_vals)

        if node is self.root:
            self.root = treeItem([middle_key], [middle_val])
            self.root.children = [left_node, right_node]
        else:
            parent = node.parent
            index = parent.children.index(node)
            parent.keys.insert(index, middle_key)
            parent.vals.insert(index, middle_val)
            parent.children[index] = left_node
            parent.children.insert(index + 1, right_node)
            if len(parent.keys) > 3:
                self.split_node(parent)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode stelt een 2-3-4 boom voor als een dict.
        -------------------------------------------------------
        Preconditite:
            De 2-3-4 boom mag niet leeg zijn
        Postconditions:
            De waarden van de zoeksleutels worden weergegeven in een dict.
        -------------------------------------------------------
        """
        def save_bst(node):
            data = {}
            # Kijkt of node niet leeg is
            if node is None:
                return None
            # Zet de root van elke boom gelijk aan de zoeksleutel van elke node
            data['root'] = node.keys
            # Kijkt of we al in een blad zitten al dan niet
            if len(node.children) > 1:
                data['children'] = []
                for child in node.children:
                    data['children'].append(save_bst(child))
            return data
        # Slaag elk node op in de dict. beginnen van de root
        return save_bst(self.root)

    def load(self, data):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode laad een dict. in als een 2-3-4 boom
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            De dict. wordt ingeladen als een 2-3-4 boom, met voor elke
            treeItem de key gelijk aan de val
        -------------------------------------------------------
        """
        def load_bst(dict):
            # Checkt of de dict niet leeg is
            if dict is None:
               return None
            # Maakt een treeItem aan voor de root, met als key en val dezelfde waarden
            treeItem = createTreeItem(dict['root'], dict['root'])
            # Kijk of er kinderen zijn
            if 'children' in dict:
                if dict['children'] is not None:
                    for child in dict['children']:
                        treeItem.children.append(load_bst(child))
                else:
                    None
            return treeItem
        # Zet de ingeladen BST gelijk aan onze self.root
        self.root = load_bst(data)


if __name__ == "__main__":
    t = TwoThreeFourTree()
    print(t.isEmpty()) # --> True
    #print(t.insertItem(createTreeItem(8,8))) # --> True
    #print(t.insertItem(createTreeItem(5,5))) # --> True
    #print(t.insertItem(createTreeItem(10,10))) # --> True
    #print(t.insertItem(createTreeItem(15,15))) # --> True
    #print(t.isEmpty()) # --> False
    #print(t.retrieveItem(5)[0])
    #print(t.retrieveItem(5)[1])
    #t.inorderTraverse(print)
    print(t.save())
    t.load({'root': [10],'children':[{'root':[5]},{'root':[11]}]})
    print(t.save())
    t.insertItem(createTreeItem(15,15))
    #print(t.deleteItem(0))
    print(t.save())
    #print(t.deleteItem(10))
    #print(t.save())