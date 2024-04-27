from pathlib import Path


class GameReader:

    def  __init__(self, file: Path = None) -> None:
        self.file = file

    
    def read(self):
        # Try to open the file, catch if it doesn't exist
        with open(self.file) as scene:
            data = scene.readlines() 
        try:

            pass
        except FileNotFoundError:
            print('The scene could not be loaded')
            return

        self.update(data)
        


    def update(self, data: list[str]):
        '''
        Updates the GUI to reflect the read scene

        :param data: The contents of the scene read in as an array
        :type data: list[str]
        '''
        choices = {}  #  key  choice, value text file
        story  = []

        i = 0
        while(True):
            if data[i] != '//':
                story.append(data[i])
                i += 1
            break
            
        while(i != len(data)):
            if data[i] == '//':
                i += 1
                continue
            # Store choices

            



