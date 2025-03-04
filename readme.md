# Rock-Paper-Scissors Game with Image Recognition

![Demo](https://i.ibb.co/5hCfLN8Y/Screenshot-24.png)

A real-time Rock-Paper-Scissors game where players use hand gestures (rock, paper, scissors) to play against the computer. The game uses **computer vision** and **machine learning** to recognize hand gestures and determine the winner.

---

## **Features**

- **Real-time Gesture Recognition**: Uses a pre-trained MobileNetV2 model to classify hand gestures.
- **Interactive UI**: Built with **Vite + React + TypeScript** and styled with **Tailwind CSS**.
- **Backend API**: Flask API deployed on **Huggingface** for gesture prediction.

---

## **Tech Stack**

- **Frontend**: Vite, React, TypeScript, Tailwind CSS
- **Backend**: Flask, TensorFlow, MobileNetV2
- **Deployment**:
  - Frontend: Vercel
  - Backend: Huggingface

---

## **Live Demo**

- **Frontend**: [https://rock-papre-scissor-ml-flask-react.vercel.app/](https://rock-papre-scissor-ml-flask-react.vercel.app/)
- **Backend API**: [https://sadek999-test.hf.space](https://sadek999-test.hf.space)

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/rayhan999/RockPapreScissor_ML-Flask-React.git
cd rock-paper-scissors
```

### **2. Set Up the Backend**

Navigate to the server folder:

```bash
cd server
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app locally:

```bash
python app.py
```

The backend will be available at [http://localhost:5000](http://localhost:5000).

### **3. Set Up the Frontend**

Navigate to the client folder:

```bash
cd ../client
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

The frontend will be available at [http://localhost:5173](http://localhost:5173).

---

## **Future Improvements**

- **Multiplayer Mode**: Allow two players to play against each other using their webcams.
- **Score Tracking**: Add a scoreboard to track wins, losses, and ties.
- **Gesture Feedback**: Provide real-time feedback if the gesture is unclear or not recognized.
- **Mobile App**: Convert the project into a mobile app using React Native or Flutter.
- **Voice Feedback**: Use text-to-speech to announce the results.
- **Advanced Model**: Train a custom model using a larger dataset for better accuracy.
- **Leaderboard**: Implement a global leaderboard to track top players.

---

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

---

## **Acknowledgments**

- Kaggle Rock-Paper-Scissors Dataset
- TensorFlow
- Vite
- Tailwind CSS
- Huggingface
- Vercel

---
