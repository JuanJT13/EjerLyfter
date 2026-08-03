class Head:
    pass


class Hand:
    pass


class Feet:
    pass


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Leg:
    def __init__(self, feet):
        self.feet = feet


class Torso:
    def __init__(self, left_arm, right_arm, left_leg, right_leg):
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human:
    def __init__(self, head, torso):
        self.head = head
        self.torso = torso


left_hand = Hand()
right_hand = Hand()

left_arm = Arm(left_hand)
right_arm = Arm(right_hand)

left_feet = Feet()
right_feet = Feet()

left_leg = Leg(left_feet)
right_leg = Leg(right_feet)

torso = Torso(
    left_arm,
    right_arm,
    left_leg,
    right_leg
)

head = Head()

human = Human(head, torso)