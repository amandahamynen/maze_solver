from app import App

class IO:
    def write(self, value, end='\n'):
        print(value, end=end)

    def read(self, prompt):
        return input(prompt)

def main():
    console_io = IO()
    app = App(console_io)
    app.run()

if __name__ == '__main__':
    main()