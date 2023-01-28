"""
    Array based implementatie van ADT Stack.
"""
class StackItemType:
    def __init__(self, value):
        self.value = value

class MyStack:
    def __init__(self, max_size):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege sack
            :param max_size staat voor de maximum groote van de stack
        -------------------------------------------------------
        Preconditie:
            max_size > 0
        Postconditie:
            Een lege stack is gemaakt
        -------------------------------------------------------
        """
        if max_size > 0:
            self.items = [None] * max_size
        else:
            return None
        self.size = 0
        return

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een stack leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de stack leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.size == 0:
            return True
        else:
            return False

    def push(self, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Voegt het element 'newitem' toe op de top van de stack.
            :param newItem staat voor het element dat op de top
             van de stack moet worden toegevoegd
        -------------------------------------------------------
        Preconditie:
            Er is nog plaats op de stack
        Postconditie:
            De stack is 1 item groter en de top
            bevat het toegevoegde item
        -------------------------------------------------------
        Return : geeft True terug als het toevoegen gelukt is
        -------------------------------------------------------
        """
        #Checkt of de stack nog niet vol zit
        if self.size == len(self.items):
            return False
        else:
            self.items[self.size] = newItem
            self.size += 1
            return True

    def pop(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Plaatst de top van een stack (volgens het LiFO principe) in
            'stackTop' en verwijderd dan deze top
        -------------------------------------------------------
        Preconditie:
            De stack bevat items
        Postconditie:
            De stack is 1 item kleiner en de top is verwijderd
        -------------------------------------------------------
        Return : geeft True terug als het verwijderen gelukt is
        -------------------------------------------------------
        """
        # Checkt of de stack al dan niet items bevat
        if self.size == 0:
            return (None, False)
        else:
            stackTop = self.items[self.size-1]
            self.items[self.size-1] = None
            self.size -= 1
            return (stackTop, True)

    def getTop(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Plaatst de top van een stack (volgens het LiFO principe) in
            'stackTop' en laat deze top ongewijzigt
        -------------------------------------------------------
        Preconditie:
            De stack moet items bevatten
        Postconditie:
            De waarde van de top van de stack word weergeven en blijft ongewijzigd
        -------------------------------------------------------
        Return : de waarde van de top van de stack terug
        -------------------------------------------------------
        """
        # Checkt of de stack al dan niet items bevat
        if self.size == 0:
            return (None, False)
        else:
            stackTop = self.items[self.size-1]
            return (stackTop, True)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Laat de volledige stack als een lijst zien
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De stack word weeergegeven als een stack met de top
            achteraan in de lijst, en de lente van de stack word geupdate
            een de None items worden verwijderd
        -------------------------------------------------------
        Return : De stack
        -------------------------------------------------------
        """
        # Verwijder de none values in de lijst
        res = []
        for val in self.items:
            if val != None:
                res.append(val)
        return res

    def load(self, lijst):
        """
        -------------------------------------------------------
        Beschrijving:
            Maakte een leeg opbject aan een vult deze met een lijst
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De lijst dat moet worden ingevalden is ingeladen
        -------------------------------------------------------
        Return : De lijst dat als stack moet worden ingeladen
        -------------------------------------------------------
        """
        self.items = lijst
        self.size = len(lijst)





# Main
if __name__ == "__main__":
    s = MyStack(2)

    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(2))
    print(s.push(4))
    print(s.push(1))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(5)
    print(s.save())

    s.load(['a','b','c'])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())