import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

const App: React.FC = () => {
  const webcamRef = useRef<Webcam>(null);
  const [prediction, setPrediction] = useState<string>('');
  const [computerMove, setComputerMove] = useState<string>('');
  const [result, setResult] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const capture = async () => {
    if (!webcamRef.current) return;

    setLoading(true);
    const imageSrc = webcamRef.current.getScreenshot();

    if (!imageSrc) {
      setLoading(false);
      return;
    }

    try {
      const blob = await fetch(imageSrc).then((res) => res.blob());
      const file = new File([blob], 'photo.jpg', { type: 'image/jpeg' });

      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('https://rockpaprescissor-ml-flask-react.onrender.com/predict', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      const userMove = response.data.prediction;
      const moves = ['rock', 'paper', 'scissors'];
      const computerMove = moves[Math.floor(Math.random() * 3)];

      setPrediction(userMove);
      setComputerMove(computerMove);

      if (userMove === computerMove) {
        setResult("It's a tie!");
      } else if (
        (userMove === 'rock' && computerMove === 'scissors') ||
        (userMove === 'paper' && computerMove === 'rock') ||
        (userMove === 'scissors' && computerMove === 'paper')
      ) {
        setResult('You win!');
      } else {
        setResult('You lose!');
      }
    } catch (error) {
      console.error('Error:', error);
      setResult('Failed to predict gesture.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex flex-col items-center justify-center text-white">
      <h1 className="text-5xl font-bold mb-8">Rock-Paper-Scissors Game</h1>
      <div className="bg-white/10 backdrop-blur-md rounded-lg p-8 shadow-2xl">
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={640}
          height={480}
          className="rounded-lg shadow-lg"
        />
        <button
          onClick={capture}
          disabled={loading}
          className="mt-6 w-full bg-white text-blue-600 py-3 px-6 rounded-lg font-semibold hover:bg-gray-100 transition-all duration-300 disabled:bg-gray-300 disabled:cursor-not-allowed"
        >
          {loading ? 'Processing...' : 'Capture and Play'}
        </button>
      </div>

      {prediction && (
        <div className="mt-8 text-center">
          <p className="text-2xl font-semibold">Your move: <span className="capitalize">{prediction}</span></p>
          <p className="text-2xl font-semibold">Computer's move: <span className="capitalize">{computerMove}</span></p>
          <p className="text-3xl font-bold mt-4">{result}</p>

        </div>
      )}
    </div>
  );
};

export default App;