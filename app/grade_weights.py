

class GradeWeights:
    """
    Specifies the weights assigned to each grade
    catefory for ENPM611. The weights can be found
    in the introductory slides and in the syllabus.
    """
    
    def __init__(self) -> None:
        self.quizzes = 5
        self.midterm = 20
        self.project = 30
        self.final = 40