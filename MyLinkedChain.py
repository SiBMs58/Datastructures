"""
    Implementatie van circulaire dubbelgelinkte ketting
"""
class Node:
    def __init__(self, data=None, prev=None, next=None):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege knoop, met als :param data, deze bevat de data
            :param prev, deze staat voor de prev pointer die wijst naar de
            vorige knoop. :param next, deze staat voor de nxt pointer en wijst
            naar de volgende knoop. Al deze waarde staat by default op None!
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Een lege node is aangemaakt
        -------------------------------------------------------
        """
        self.data = data
        self.prev = prev
        self.next = next

class LinkedChain:
    def __init__(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege lijst
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Een lege lijst is gemaakt
        -------------------------------------------------------
        """
        self.head = None
        self.size = 0

    def destroyList(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Wist een lijst
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De ketting wordt verwijderd
        -------------------------------------------------------
        """
        for i in range(self.getLength()):
            self.delete(self.getLength())
        del self

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een lijst leeg is
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Er word ge-returned of de lijst al dan niet leeg is
        -------------------------------------------------------
        """
        if self.size == 0:
            return True
        else:
            return False

    def getLength(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Geeft het aantal elementen in de lijst
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            Het aantal elementen word ge-returned
        -------------------------------------------------------
        """
        return self.size

    def insert(self, positie, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
           Voegt het element: param 'newItem' toe
           op :param 'positie' in een lijst
        -------------------------------------------------------
        Preconditie:
            De opgegeven positie moet geldig zijn d.w.z.
            niet groter dan de size+1 of kleiner dan 1
        Postconditie:
            Het element newItem wordt toegevoegd aan
            de gelinkte ketting op de opgegeven positie
        -------------------------------------------------------
        Return : Geeft True terug indien het toevoegen is gelukt, anders False
        -------------------------------------------------------
        """
        # Checkt of opgegeven positie geldig is, zo ja dan word er WEL toegevoegd
        if 1 <= positie <= (self.getLength()+1):
            # Checkt of de chain leeg is
            if not self.head:
                # Als de chain leeg is dan creëren we een nieuwe knoop,
                # en zetten we de pointers van deze knoop naar zichzelf
                self.head = Node(newItem)
                self.head.prev = self.head
                self.head.next = self.head
                # Tel 1 op bij de size
                self.size += 1
                return True
            # Checkt op een insert op de eerste positie
            elif (positie - 1) == 0:
                # Checkt of de chain leeg is
                if not self.head:
                    # Als de chain leeg is dan creëren we een nieuwe knoop,
                    # en zetten we de pointers van deze knoop naar zichzelf
                    self.head = Node(newItem)
                    self.head.prev = self.head
                    self.head.next = self.head
                    # Tel 1 op bij de size
                    self.size += 1
                    return True
                else:
                    new_node = Node(newItem, self.head.prev, self.head)
                    self.head.prev.next = new_node
                    self.head.prev = new_node
                    self.head = new_node
                    # Tel 1 op bij de size
                    self.size += 1
                    return True
            # Anders dan 'loopen' we door de chain tot we aan de knoop komen op :param 'positie'
            # En voegen we de nieuwe knoop erna toe
            else:
                current = self.head
                i = 1
                while current.next != self.head and i < positie-1:
                    current = current.next
                    i += 1
                new_node = Node(newItem, current, current.next)
                current.next.prev = new_node
                current.next = new_node
                # Tel 1 op bij de size
                self.size += 1
                return True
        # Hier wordt er NIET toegevoegd
        else:
            return False

    def delete(self, positie):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijdert het element op: param 'positie' uit een lijst
        -------------------------------------------------------
        Preconditie:
            De opgegeven positie moet geldig zijn d.w.z.
            niet groter dan de size of een niet kleiner dan 1,
            eveneens moet de ketting ook items bevatten.
        Postconditie:
            Het element op de opgegeven positie wordt verwijderd
        -------------------------------------------------------
        Return : Geeft True terug indien het verwijderen is gelukt, anders False
        -------------------------------------------------------
        """
        # Checkt of opgegeven positie geldig is
        if 1 <= positie <= self.getLength():
            # Als de positie 1 is dan verwijderd het de head
            if positie == 1:
                if self.head == self.head.next:
                    self.head = None
                    # Trek 1 af bij de size
                    self.size -= 1
                    return True
                else:
                    self.head.prev.next = self.head.next
                    self.head.next.prev = self.head.prev
                    self.head = self.head.next
                    # Trek 1 af bij de size
                    self.size -= 1
                    return True
            # Anders traversen we de chain tot dat we de positie bereiken
            else:
                current = self.head.next
                i = 1
                while current != self.head and i < positie-1:
                    current = current.next
                    i += 1
                if current != self.head:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    # Trek 1 af bij de size
                    self.size -= 1
                    return True
        else:
            return False

    def retrieve(self, positie):
        """
        -------------------------------------------------------
        Beschrijving:
            Plaatst het element op :param 'positie' van een lijst
            in :param 'dataItem'
        -------------------------------------------------------
        Preconditie:
            De opgegeven positie moet geldig zijn d.w.z.
            niet groter dan de size of een niet kleiner dan 1,
            eveneens moet de ketting ook items bevatten.
        Postconditie:
            Het 'dataItem' is gelijk aan het element
            op de opgevraagde positie
        -------------------------------------------------------
        Return : Het dataItem + True indien het gelukt is anders False
        -------------------------------------------------------
        """
        # Checkt of opgegeven positie geldig is
        if 1 <= positie <= self.getLength():
            dataItem = self.head
            i = 1
            while dataItem.next != self.head and i < positie:
                dataItem = dataItem.next
                i += 1
            if i == positie:
                return dataItem.data, True
            else:
                return None, False
        else:
            return None, False



    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Laat de volledige gelinkte ketting als een lijst zien
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De gelinkte ketting wordt weergegeven als een lijst met de head
            vooraan in de lijst
        -------------------------------------------------------
        Return : De gelinkte ketting weergeven als een lijst
        -------------------------------------------------------
        """
        list = []
        for i in range(self.getLength()):
            list.append(self.head.data)
            self.head = self.head.next
        return list

    def load(self, lijst):
        """
        -------------------------------------------------------
        Beschrijving:
            Maakte een leeg gelinkte ketting aan een vult deze met een lijst
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De lijst dat moet worden ingeladen is ingeladen als een circulaire dubbel gelinkte ketting
        -------------------------------------------------------
        Return : De lijst dat als gelinkte ketting moet worden ingeladen
        -------------------------------------------------------
        """
        newLinkedChain = LinkedChain()
        # Loading in the list as a doubly linked chain
        for i in range(len(lijst)):
            newLinkedChain.insert(i+1, lijst[i])
        # Setting our self equal to our newLinkedChain
        for i in range(newLinkedChain.getLength()):
            self.head = newLinkedChain.head
            self.size = newLinkedChain.size

# Main
if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())
    print(l.getLength())
    print(l.retrieve(4)[1])
    print(l.insert(4,500))
    print(l.isEmpty())
    print(l.insert(1,500))
    print(l.retrieve(1)[0])
    print(l.retrieve(1)[1])
    print(l.save())
    print(l.insert(1,600))
    print(l.save())
    l.load([10,-9,15])
    l.insert(3,20)
    print(l.delete(0))
    print(l.save())
    print(l.delete(1))
    print(l.save())