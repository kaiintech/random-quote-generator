import random

quotes = {
    "Albert Einstein": "Life is like riding a bicycle. To keep your balance you must keep moving.",
    "Maya Angelou": "You will face many defeats in life, but never let yourself be defeated.",
    "Oscar Wilde": "Be yourself; everyone else is already taken.",
    "Mark Twain": "The secret of getting ahead is getting started.",
    "Nelson Mandela": "It always seems impossible until it's done.",
    "Confucius": "It does not matter how slowly you go as long as you do not stop.",
    "Steve Jobs": "Stay hungry, stay foolish.",
    "Mother Teresa": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
    "Benjamin Franklin": "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
    "Rumi": "The wound is the place where the Light enters you.",
    "Helen Keller": "Alone we can do so little; together we can do so much.",
    "Dalai Lama": "Happiness is not something ready made. It comes from your own actions.",
    "Aristotle": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
    "Buddha": "What we think, we become.",
    "Socrates": "The unexamined life is not worth living.",
    "Leonardo da Vinci": "Learning never exhausts the mind.",
    "Walt Disney": "The way to get started is to quit talking and begin doing.",
    "Eleanor Roosevelt": "The future belongs to those who believe in the beauty of their dreams.",
    "Henry Ford": "Whether you think you can, or you think you can't, you're right.",
    "Marcus Aurelius": "You have power over your mind - not outside events. Realize this, and you will find strength.",
    "Seneca": "It is not the man who has too little, but the man who craves more, that is poor.",
    "Epictetus": "It's not what happens to you, but how you react to it that matters.",
    "Plato": "Courage is knowing what not to fear.",
    "Ralph Waldo Emerson": "Do not go where the path may lead, go instead where there is no path and leave a trail.",
    "Friedrich Nietzsche": "He who has a why to live can bear almost any how.",
    "Lao Tzu": "The journey of a thousand miles begins with a single step.",
    "Mahatma Gandhi": "Be the change that you wish to see in the world.",
    "Carl Jung": "Who looks outside, dreams; who looks inside, awakes.",
    "Victor Hugo": "Even the darkest night will end and the sun will rise.",
    "Charles Dickens": "Have a heart that never hardens, and a temper that never tires, and a touch that never hurts.",
    "William Shakespeare": "We know what we are, but know not what we may be.",
    "Khalil Gibran": "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars.",
    "Bruce Lee": "Absorb what is useful, discard what is not, add what is uniquely your own.",
    "Alan Watts": "Trying to define yourself is like trying to bite your own teeth."
}


print('>> Welcome to the Inspirational Quote Generator. type press "q" to quit <<\n')

while True:
    user_input = input('Press Enter to generate a quote ')

    if user_input.lower() == 'q':
        print('Goodbye for now. Stay inspired.')
        break

    author, quote = random.choice(list(quotes.items()))
    print(f"\n{author}: \"{quote}\"\n")


