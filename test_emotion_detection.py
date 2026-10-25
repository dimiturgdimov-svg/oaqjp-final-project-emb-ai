"""Integration tests for the course emotion detection service."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check all five emotion categories against the specified examples."""

    def test_joy(self):
        """Recognize the joy example."""
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    def test_anger(self):
        """Recognize the anger example."""
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

    def test_disgust(self):
        """Recognize the disgust example."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Recognize the sadness example."""
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

    def test_fear(self):
        """Recognize the fear example."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
