Installation
Clone the repository:

bash
Copier
Modifier
git clone https://github.com/ben-chaaben-nader/puzzle_game.git
Navigate to the project directory:

bash
Copier
Modifier
cd puzzle_game
Install dependencies:

bash
Copier
Modifier
pip install -r requirements.txt
Run the game:

bash
Copier
Modifier
python src/game.py
📁 Project Structure
bash
Copier
Modifier
puzzle_game/
├── assets/
│   ├── background.mp3         # Background music
│   ├── click.wav              # Click sound
│   ├── win.wav                # Win sound
│   └── photo.jpg              # Puzzle image
├── src/
│   └── game.py                # Main game logic
├── dist/                      # Compiled files
├── requirements.txt           # Dependencies list
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore file
└── game.spec                  # PyInstaller spec file
🔊 Sound and Assets
All game assets (image, music, and sounds) are placed in the assets/ directory for better organization.

🎮 How to Play
Click on the puzzle tiles to swap their positions.

Arrange the image back to its original form.

Enjoy background music and sound effects as you play.

When you complete the puzzle, a win sound will be triggered.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

💡 Future Improvements
Add different difficulty levels.

Implement a timer and scoring system.

Allow the user to upload custom images for the puzzle.

🤝 Contributing
Feel free to fork this project and submit pull requests. Contributions are welcome!

📝 Author
Nader Ben Chabane
chaben.nader@gmail.com
InfinityTech Solutions