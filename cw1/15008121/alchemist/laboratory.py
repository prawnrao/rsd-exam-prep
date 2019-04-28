class Laboratory:

    def __init__(self, dict_lab):
        """ Instantiates a Laboratory object.

        Parameters
        ----------
        dict_lab: dictionary
            Two shelf laboratory in dictionary form. 
        """
        if (len(dict_lab) != 2):
            raise TypeError('The number of shelves differs from 2.')

        if not dict_lab['lower']:
            raise TypeError('The lower shelf is empty.')

        if not dict_lab['upper']:
            raise TypeError('The upper shelf is empty.')

        self.lower = dict_lab['lower']
        self.upper = dict_lab['upper']

    @staticmethod
    def can_react(substance1, substance2):
        """ Returns true if one of the substances is the 'anti' of
        the other.

        Parameters
        ----------
        substance1: str
            Name of a substance, such as hydrogen or oxygen

        substance2: str
            Name of a substance, such as antihydrogen or antioxygen

        Returns
        -------
        boolean
            True: substances can react
            False: substances cannot react
        """
        if substance1.startswith('antianti'):
            raise Exception('antianti substances cannot exist')

        if substance2.startswith('antianti'):
            raise Exception('antianti substances cannot exist')

        is_anti_substance1 = (substance1 == "anti" + substance2)
        is_anti_substance2 = (substance2 == "anti" + substance1)
        return is_anti_substance1 or is_anti_substance2

    @staticmethod
    def update_shelves(shelf1, shelf2, substance1, substance2_index):
        """ Generates the new shelves by removing the two substances
        that can react.

        Parameters
        ----------
        shelf1: list
            List of substances (str)

        shelf2: list
            List of substances (str)

        substance1: str
            Name of a substance

        substance2_index: int
            Index of a substance that can react with substance1

        Returns
        -------
        list, list
            Updated shelf1 and shelf2     
        """
        index1 = shelf1.index(substance1)
        shelf1 = shelf1[:index1] + shelf1[index1 + 1:]
        shelf2 = shelf2[:substance2_index] + shelf2[substance2_index + 1:]
        return shelf1, shelf2

    def do_a_reaction(shelf1, shelf2):
        """  For each substance in a shelf, respective 'anti'
        substances are found, one of which is reacted at random.

        Parameters
        ----------
        shelf1: list
            List of substances (str)

        shelf2: list
            List of substances (str)

        Returns
        -------
        list, list
            Updated shelf1 and shelf2
        """
        import random
        for substance1 in shelf1:
            possible_targets = [i for i, target in enumerate(
                shelf2) if Laboratory.can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                substance2_index = random.choice(possible_targets)
                return Laboratory.update_shelves(
                    shelf1, shelf2, substance1, substance2_index)
        return shelf1, shelf2

    def run_full_experiment(self, num_reactions=False):
        """ 

        Parameters
        ----------
        num_reactions: boolean
            Default value is false.

        Returns
        -------
        If num_reactions is False: list, list
            Updated lower and upper shelves of the Laboratory object.

        If num_reactions is True: int
            The number of reactions that occured.
        """
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = Laboratory.do_a_reaction(
                self.lower, self.upper)
            if shelf1_new != self.lower:
                count += 1
            ended = (shelf1_new == self.lower) and (shelf2_new == self.upper)
            self.lower, self.upper = shelf1_new, shelf2_new
        if num_reactions:
            return(count)
        else:
            return self.lower, self.upper
