from __future__ import annotations

import random
from typing import Optional

from app.utils.prompt import Prompt


class PseudoLLM:
    def __init__(self, seed: int | None = None) -> None:
        self.random = random.Random(seed)

    def generate(self, prompt: Prompt) -> str:
        # Extract user details from prompt
        user_name = ""
        zodiac = ""
        language = "en"
        
        if "User:" in prompt.user:
            try:
                user_name = prompt.user.split("User:")[1].split("\n")[0].strip()
            except:
                user_name = "dear friend"
        
        if "Zodiac:" in prompt.user:
            try:
                zodiac = prompt.user.split("Zodiac:")[1].split("\n")[0].strip()
            except:
                zodiac = ""
        
        if "Language:" in prompt.user:
            try:
                language = prompt.user.split("Language:")[1].split("\n")[0].strip().lower()
            except:
                language = "en"
        
        # Generate dynamic insight based on language
        if language == "hi":
            return self._generate_dynamic_hindi_insight(user_name, zodiac)
        else:
            return self._generate_dynamic_english_insight(user_name, zodiac)
    
    def _generate_dynamic_english_insight(self, user_name: str, zodiac: str) -> str:
        """Generate dynamic English insight using templates and user data"""
        
        # Zodiac-specific traits and energies
        zodiac_data = {
            "Aries": {
                "traits": ["bold", "energetic", "pioneering", "confident", "spontaneous"],
                "elements": ["fire", "passion", "leadership", "courage", "initiative"],
                "actions": ["take charge", "lead boldly", "embrace challenges", "trust instincts", "act decisively"]
            },
            "Taurus": {
                "traits": ["steady", "reliable", "patient", "grounded", "practical"],
                "elements": ["earth", "stability", "comfort", "persistence", "security"],
                "actions": ["stay grounded", "build steadily", "find comfort", "be patient", "trust process"]
            },
            "Gemini": {
                "traits": ["curious", "adaptable", "communicative", "versatile", "expressive"],
                "elements": ["air", "communication", "flexibility", "learning", "connection"],
                "actions": ["communicate clearly", "stay curious", "adapt quickly", "share ideas", "connect meaningfully"]
            },
            "Cancer": {
                "traits": ["intuitive", "nurturing", "emotional", "protective", "empathetic"],
                "elements": ["water", "emotions", "intuition", "care", "boundaries"],
                "actions": ["trust intuition", "nurture others", "set boundaries", "feel deeply", "care wisely"]
            },
            "Leo": {
                "traits": ["creative", "charismatic", "generous", "confident", "dramatic"],
                "elements": ["fire", "creativity", "leadership", "generosity", "warmth"],
                "actions": ["shine brightly", "lead with warmth", "create beauty", "share generously", "inspire others"]
            },
            "Virgo": {
                "traits": ["analytical", "methodical", "practical", "detail-oriented", "helpful"],
                "elements": ["earth", "analysis", "improvement", "service", "precision"],
                "actions": ["analyze carefully", "improve systems", "help others", "pay attention", "serve practically"]
            },
            "Libra": {
                "traits": ["diplomatic", "balanced", "fair", "harmonious", "gracious"],
                "elements": ["air", "balance", "harmony", "justice", "beauty"],
                "actions": ["seek balance", "create harmony", "be fair", "find beauty", "compromise wisely"]
            },
            "Scorpio": {
                "traits": ["intense", "passionate", "transformative", "mysterious", "resourceful"],
                "elements": ["water", "transformation", "depth", "passion", "mystery"],
                "actions": ["embrace intensity", "transform challenges", "dive deep", "feel passionately", "uncover truth"]
            },
            "Sagittarius": {
                "traits": ["optimistic", "adventurous", "philosophical", "generous", "free-spirited"],
                "elements": ["fire", "adventure", "wisdom", "optimism", "freedom"],
                "actions": ["explore boldly", "stay optimistic", "seek wisdom", "embrace adventure", "share freely"]
            },
            "Capricorn": {
                "traits": ["disciplined", "responsible", "ambitious", "practical", "patient"],
                "elements": ["earth", "discipline", "ambition", "structure", "achievement"],
                "actions": ["build systematically", "stay disciplined", "achieve goals", "be responsible", "plan wisely"]
            },
            "Aquarius": {
                "traits": ["innovative", "independent", "humanitarian", "progressive", "unique"],
                "elements": ["air", "innovation", "freedom", "progress", "community"],
                "actions": ["innovate boldly", "think uniquely", "help humanity", "embrace progress", "stay independent"]
            },
            "Pisces": {
                "traits": ["intuitive", "compassionate", "artistic", "spiritual", "gentle"],
                "elements": ["water", "intuition", "compassion", "creativity", "spirituality"],
                "actions": ["trust intuition", "show compassion", "create artfully", "feel deeply", "heal gently"]
            }
        }
        
        # Get zodiac data or use general traits
        if zodiac in zodiac_data:
            data = zodiac_data[zodiac]
        else:
            data = {
                "traits": ["wise", "intuitive", "balanced", "caring", "authentic"],
                "elements": ["wisdom", "intuition", "balance", "care", "authenticity"],
                "actions": ["trust yourself", "stay balanced", "care deeply", "be authentic", "grow wisely"]
            }
        
        # Dynamic templates
        templates = [
            f"Today, {user_name}, your {self.random.choice(data['traits'])} nature will help you {self.random.choice(data['actions'])}. Your {self.random.choice(data['elements'])} energy creates positive ripples.",
            f"{user_name}, embrace your {self.random.choice(data['traits'])} spirit today. The {self.random.choice(data['elements'])} around you supports your journey to {self.random.choice(data['actions'])}.",
            f"Your {self.random.choice(data['traits'])} essence shines brightly today, {user_name}. Trust in your ability to {self.random.choice(data['actions'])} with {self.random.choice(data['elements'])}.",
            f"Today calls for your {self.random.choice(data['traits'])} wisdom, {user_name}. Let your {self.random.choice(data['elements'])} guide you as you {self.random.choice(data['actions'])}.",
            f"{user_name}, your {self.random.choice(data['traits'])} nature is your greatest strength today. Channel your {self.random.choice(data['elements'])} to {self.random.choice(data['actions'])}."
        ]
        
        # Choose a template and add personalized touches
        base_insight = self.random.choice(templates)
        
        # Add personalized endings
        endings = [
            " Stay open to unexpected blessings.",
            " Your positive energy creates meaningful connections.",
            " Trust the timing of your life's journey.",
            " Remember to celebrate your progress.",
            " Your kindness makes a difference today.",
            " Embrace the present moment with gratitude.",
            " Your authentic self attracts the right opportunities.",
            " Small actions create significant impact."
        ]
        
        if self.random.random() < 0.7:
            base_insight += self.random.choice(endings)
        
        return base_insight
    
    def _generate_dynamic_hindi_insight(self, user_name: str, zodiac: str) -> str:
        """Generate dynamic Hindi insight using templates and user data"""
        
        # Zodiac-specific traits and energies in Hindi
        zodiac_data = {
            "Aries": {
                "traits": ["साहसी", "ऊर्जावान", "अग्रणी", "आत्मविश्वासी", "सहज"],
                "elements": ["अग्नि", "जोश", "नेतृत्व", "साहस", "पहल"],
                "actions": ["नेतृत्व करें", "साहस दिखाएं", "चुनौतियों का सामना करें", "प्रवृत्ति पर भरोसा करें", "निर्णायक बनें"]
            },
            "Taurus": {
                "traits": ["स्थिर", "विश्वसनीय", "धैर्यवान", "जमीनी", "व्यावहारिक"],
                "elements": ["पृथ्वी", "स्थिरता", "आराम", "दृढ़ता", "सुरक्षा"],
                "actions": ["स्थिर रहें", "धीरे-धीरे बनाएं", "आराम खोजें", "धैर्य रखें", "प्रक्रिया पर भरोसा करें"]
            },
            "Gemini": {
                "traits": ["जिज्ञासु", "अनुकूलनीय", "संचारी", "बहुमुखी", "अभिव्यंजक"],
                "elements": ["वायु", "संचार", "लचीलापन", "सीखना", "जुड़ाव"],
                "actions": ["स्पष्ट संचार करें", "जिज्ञासु बनें", "त्वरित अनुकूलन करें", "विचार साझा करें", "सार्थक जुड़ाव बनाएं"]
            },
            "Cancer": {
                "traits": ["सहज", "पोषक", "भावुक", "सुरक्षात्मक", "सहानुभूतिपूर्ण"],
                "elements": ["जल", "भावनाएं", "अंतर्ज्ञान", "देखभाल", "सीमाएं"],
                "actions": ["अंतर्ज्ञान पर भरोसा करें", "दूसरों का पोषण करें", "सीमाएं निर्धारित करें", "गहराई से महसूस करें", "समझदारी से देखभाल करें"]
            },
            "Leo": {
                "traits": ["रचनात्मक", "करिश्माई", "उदार", "आत्मविश्वासी", "नाटकीय"],
                "elements": ["अग्नि", "रचनात्मकता", "नेतृत्व", "उदारता", "गर्मजोशी"],
                "actions": ["चमकें", "गर्मजोशी से नेतृत्व करें", "सुंदरता बनाएं", "उदारता से साझा करें", "दूसरों को प्रेरित करें"]
            },
            "Virgo": {
                "traits": ["विश्लेषणात्मक", "व्यवस्थित", "व्यावहारिक", "विवरण-उन्मुख", "सहायक"],
                "elements": ["पृथ्वी", "विश्लेषण", "सुधार", "सेवा", "सटीकता"],
                "actions": ["सावधानी से विश्लेषण करें", "सिस्टम सुधारें", "दूसरों की मदद करें", "विवरण पर ध्यान दें", "व्यावहारिक सेवा करें"]
            },
            "Libra": {
                "traits": ["कूटनीतिक", "संतुलित", "निष्पक्ष", "सामंजस्यपूर्ण", "अनुग्रही"],
                "elements": ["वायु", "संतुलन", "सामंजस्य", "न्याय", "सुंदरता"],
                "actions": ["संतुलन खोजें", "सामंजस्य बनाएं", "निष्पक्ष बनें", "सुंदरता खोजें", "समझदारी से समझौता करें"]
            },
            "Scorpio": {
                "traits": ["तीव्र", "भावुक", "रूपांतरणकारी", "रहस्यमय", "संसाधनपूर्ण"],
                "elements": ["जल", "रूपांतरण", "गहराई", "जुनून", "रहस्य"],
                "actions": ["तीव्रता को अपनाएं", "चुनौतियों को बदलें", "गहराई में जाएं", "जुनून से महसूस करें", "सत्य खोजें"]
            },
            "Sagittarius": {
                "traits": ["आशावादी", "साहसिक", "दार्शनिक", "उदार", "स्वतंत्र"],
                "elements": ["अग्नि", "साहस", "बुद्धि", "आशावाद", "स्वतंत्रता"],
                "actions": ["साहस से खोजें", "आशावादी बनें", "बुद्धि खोजें", "साहस को अपनाएं", "स्वतंत्र रूप से साझा करें"]
            },
            "Capricorn": {
                "traits": ["अनुशासित", "जिम्मेदार", "महत्वाकांक्षी", "व्यावहारिक", "धैर्यवान"],
                "elements": ["पृथ्वी", "अनुशासन", "महत्वाकांक्षा", "संरचना", "उपलब्धि"],
                "actions": ["व्यवस्थित रूप से बनाएं", "अनुशासित रहें", "लक्ष्य प्राप्त करें", "जिम्मेदार बनें", "समझदारी से योजना बनाएं"]
            },
            "Aquarius": {
                "traits": ["नवाचारी", "स्वतंत्र", "मानवतावादी", "प्रगतिशील", "अनूठा"],
                "elements": ["वायु", "नवाचार", "स्वतंत्रता", "प्रगति", "समुदाय"],
                "actions": ["साहस से नवाचार करें", "अनूठा सोचें", "मानवता की मदद करें", "प्रगति को अपनाएं", "स्वतंत्र रहें"]
            },
            "Pisces": {
                "traits": ["सहज", "दयालु", "कलात्मक", "आध्यात्मिक", "कोमल"],
                "elements": ["जल", "अंतर्ज्ञान", "दया", "रचनात्मकता", "आध्यात्मिकता"],
                "actions": ["अंतर्ज्ञान पर भरोसा करें", "दया दिखाएं", "कलात्मक रूप से बनाएं", "गहराई से महसूस करें", "कोमलता से उपचार करें"]
            }
        }
        
        # Get zodiac data or use general traits
        if zodiac in zodiac_data:
            data = zodiac_data[zodiac]
        else:
            data = {
                "traits": ["बुद्धिमान", "सहज", "संतुलित", "दयालु", "प्रामाणिक"],
                "elements": ["बुद्धि", "अंतर्ज्ञान", "संतुलन", "देखभाल", "प्रामाणिकता"],
                "actions": ["अपने आप पर भरोसा करें", "संतुलित रहें", "गहराई से देखभाल करें", "प्रामाणिक बनें", "समझदारी से बढ़ें"]
            }
        
        # Dynamic Hindi templates
        templates = [
            f"आज, {user_name}, आपकी {self.random.choice(data['traits'])} प्रकृति आपको {self.random.choice(data['actions'])} में मदद करेगी। आपकी {self.random.choice(data['elements'])} ऊर्जा सकारात्मक प्रभाव बनाती है।",
            f"{user_name}, आज अपनी {self.random.choice(data['traits'])} भावना को अपनाएं। आपके आसपास की {self.random.choice(data['elements'])} आपकी यात्रा में सहायता करती है।",
            f"आपकी {self.random.choice(data['traits'])} आत्मा आज चमकती है, {user_name}। अपनी {self.random.choice(data['elements'])} के साथ {self.random.choice(data['actions'])} की क्षमता पर भरोसा करें।",
            f"आज आपकी {self.random.choice(data['traits'])} बुद्धि की आवश्यकता है, {user_name}। अपनी {self.random.choice(data['elements'])} को अपना मार्गदर्शक बनने दें।",
            f"{user_name}, आपकी {self.random.choice(data['traits'])} प्रकृति आज आपकी सबसे बड़ी ताकत है। अपनी {self.random.choice(data['elements'])} को {self.random.choice(data['actions'])} के लिए चैनल करें।"
        ]
        
        # Choose a template and add personalized touches
        base_insight = self.random.choice(templates)
        
        # Add personalized Hindi endings
        endings = [
            " अप्रत्याशित आशीर्वादों के लिए खुले रहें।",
            " आपकी सकारात्मक ऊर्जा सार्थक संबंध बनाती है।",
            " अपने जीवन की यात्रा के समय पर भरोसा करें।",
            " अपनी प्रगति का जश्न मनाना याद रखें।",
            " आज आपकी दया एक फर्क पड़ता है।",
            " कृतज्ञता के साथ वर्तमान क्षण को अपनाएं।",
            " आपका प्रामाणिक स्व सही अवसरों को आकर्षित करता है।",
            " छोटे कार्य महत्वपूर्ण प्रभाव बनाते हैं।"
        ]
        
        if self.random.random() < 0.7:
            base_insight += self.random.choice(endings)
        
        return base_insight


