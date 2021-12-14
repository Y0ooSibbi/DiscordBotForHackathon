import random
yes_no = ["A thousand times, yes!",
"A million times, yes!",
"Count me in!",
"No problem. I’m always happy to help.",
"Aye, sir!",
"I think we have a consensus.",
"I would like to express my full approval.",
"I’d be delighted.",
"Damn straight.",
"As you say.",
"Goddamn right!",
"I agree to the fullest!",
"Just say the word and I shall be there.",
"I agree.",
"Whatever! Let’s do this!",
"Let’s do it.",
"I’m happy to serve!",
"I gladly concur.",
"As long as it’s not impossible, I’d be glad to do it.",
"True enough!",
"Gotcha.",
"I’d be honored.",
"I know that you’re speaking the truth.",
"I couldn’t agree more.",
"I couldn’t disagree less.",
"It would be my honor.",
"It can’t be help then.",
"I take your point.",
"I concur.",
"That is true.",
"I believe we have come to an agreement.",
"You owe me one.",
"My pleasure.",
"The deal is on!",
"I can’t argue with that!",
"We share the same sentiments.",
"Okey-dokey!",
"I’m at your behest.",
"Aye aye, captain!",
"I was born for this!",
"That would be a Y-E-S!",
"You just stole the words out of my mouth.",
"Right on, brother/sister.",
"Definitely not NO.",
"That’s the way!",
"Your wish is my command.",
"I guess it’s up to me now.",
"Then I’m giving you the go signal.",
"Hahaha, that’s true.",
"Great idea!",
"I’ll do anything for you.",
"I’m leaning towards what you desire.",
"You stole my brain!",
"You lead, I follow.",
"Amen to that!",
"I acquiesce to your demand.",
"I do not disagree.",
"Your idea nearly reflects all of my thoughts.",
"I have no option but to regrettably agree to this foolish idea of yours.",
"My belief is that you speak the truth.",
"I subscribe to your idea.",
"Let’s do a pinky swear.",
"I give you my blessing.",
"It would be of great honor to me.",
"My answer is in the affirmative.",
"I hereby acknowledge what you’ve just said.",
"I give you my seal of approval.",
"What’s the opposite of no?",
"If I was a regular jerk, I’d say no to this one.",
"Is the mitochondria the powerhouse of the cell?",
"My two thumbs are standing in salute.",
"Is the sun hot?",
"My guts tell me that you are worth all the trouble.",
"Do fishes swim?",
"Something tells me I should trust you. But, I think it's just your words.",
"Is one plus one equal to two?",
"It appears that you have read my mind.",
"Are boogers salty?",
"Come on, humor me.",
"Do pigeons fly?",
"Tell me more.",
"Is the pope catholic?",
"Do vacuum cleaners suck?",
"Is water wet?",
"Is the hypotenuse the longest side of a triangle?",
"Does a bear live in the woods?",
"I’ll answer you with my favorite ‘Y’ word—Yes!",
"Is the sky blue?",
"I totally ‘scored’ getting asked by you. Yes!",
"How do you spell yes?",
"Would you take ‘yes’ for an answer?",
"I haven’t said no yet, right?",
"Would I be too tall for you if I were standing on cloud 9?",
"Am I not holding my two thumbs up?",
"There’s a 100% chance that I’m going say yes to that one.",
"Like a dog wagging its tail in excitement!",
"Oh yeah, baby!",
"I would love to, but there’s got to be a way to do it without killing myself.",
"Just in case, can I bring my pet monkey?",
"I have examined your worthwhile view thoroughly. After close deliberation, I would say that I vehemently concur to the bases of your belief, and share your ideas on the said premise.",
"My enthusiastic nodding says it all.",
"I love you so much, that I’ll only agree with anything you say.",
"You deserve a standing ovation for that idea.",
"There is a huge possibility that you are correct.",
"You deserve a round of applause.",
"Yes, my liege.",
"Due to the unlikelihood of an error on your part, I am forced to toss my lot in with you.",
"I’m leaning towards yes, but what’s in it for me?",
"I was hoping you’d ask.",
"I’ll put my life on the line just for you.",
"Upon close examination of the aforementioned data, I wholeheartedly accept your conclusion as plausible.",
"The smile on my face says it all!",
"Go on, I’m listening intently.",
"I firmly believe that our views about the subject matter at hand are very similar.",
"You are going to regret asking me this.",
"You’ve gotta be kidding me!",
"You’re a perfect 10!",
"The answer is a resounding yes!",
"I would love to say yes, but my dog told me to say no.",
"Sorry, I can’t. I have to walk my unicorn.",
"Only if you give me a million bucks!",
"I would, but I’m a cat!",
"I’m pretty sure there’s someone a lot stupider who would enjoy doing that instead.",
"My advisors have come to a unanimous decision, and it’s a—NO!",
"In this world, there are countless of cool things to do. Unfortunately, your idea does fall into such category.",
"The voices in my head are asking me to say ‘no’ to this one.",
"Sweetie, you can’t afford me.",
"I have a strict ‘no deals with the devil’ policy.",
"That’s such a funny joke! HAHAHAHA!",
"I’d rather swallow a pillow.",
"It’s N to the O!",
"I’d rather pull out each of my teeth and swallow them all together.",
"I would say no even if you kiss my butt.",
"You know what season it is? It’s the season of NO!",
"That sounds like effort, so no.",
"Does it involve me moving from where I am right now? If the answer is yes, then I would have to say no.",
"You should know my answer by the look of disgust on my face.",
"I would love to say yes, but I actually wouldn’t love to say yes.",
"I can’t today, sorry. My brother’s friend’s pet lizard just died, and yeah, it was tragic.",
"My apologies, but my schedule is packed with better things.",
"Give me an ‘N.’ Give me an ‘O.’ Give me an ‘N-O!’",
"Not today, Satan! Not today.",
"Alas, such a task is no match for my incompetency.",
"I’m too lazy to even breath, so why would you ask that of me?!",
"I think I’ll just find a lake full of piranhas to jump into instead.",
"Please email your concern to ‘idontcare.com’ and I’ll send you my decision in a hundred years.",
"I would love to, but unfortunately...no.",
"It’s not a priority for me this time.",
"I do not approve!",
"I’m sorry, but you’re not worth the trouble.",
"Negative!",
"My answer is a resounding no!",
"There’s a hundred percent chance that I’m going to say ‘no’ to this one.",
"Offer declined!",
"No means no, now let it go.",
"I think not.",
"Frankly, my dear—no!",
"I’ve already booked into something else. Sorry.",
"I would prefer another option.",
"Definitely not me!",
"You should rethink your idea.",
"I’m busy, scram!",
"I shall not!",
"There are worse things I could say ‘yes’ to. I just can’t think of any at the moment.",
"No way, Jose.",
"Why, heavens no!",
"Oh, hell no!",
"I wasn’t born for this.",
"I find that idea undesirable.",
"Unfortunately, we don’t share the same sentiments.",
"I have a bad feeling about this, so no.",
"My parents said no.",
"No no no no no no no no no no no!",
"Sorry, but I’m trying to limit my commitments this year.",
"On a scale of maybe to absolutely, I would say—absolutely not!",
"In another life, perhaps?",
"My two thumbs are pointing down, right?",
"Sorry, but I will have to sit this one out.",
"What part of the word ‘no’ do you not understand?",
"I do not subscribe to that notion.",
"Request rejected!",
"I’m disinclined to acquiesce to your request.",
"My future self says no!",
"I would only say ‘yes’ if hell has already frozen over.",
"Your idea is not compatible with me.",
"It’s that time of the year when I usually always say no.",
"Regrettably, I’m a no-man!",
"Liar, liar, panties on fire!",
"My parents would disown me if I did that.",
"My instincts are telling me that I’m not suitable for this.",
"I don’t have an iota of bandwidth left in my brain.",
"Life is too short to be doing stupid things. And by stupid things, I meant you!",
"I’m going to have to flex my ‘no’ muscle on this one.",
"Life is too short to do things that you don’t love.",
"My word of the year is ‘rest’, so I really can’t fit another thing in.",
"My schedule is up in the air right now. Can you not see it gently wafting down the corridor?",
"Me not loving your idea means that I’m not the right person for it.",
"Shop is closed! Come back again tomorrow.",
"Sorry, better luck next time.",
"It’s not that I’m too good to do what you want. It’s just that it’s too bad for me to do.",
"Saying ‘yes’ would surely cause the slow, withering death of soul.",
"Oh, I wish there were two of me.",
"What’s the opposite of yes?",
"Is a dog a human?",
"That sounds like fun, but I am going to be extremely busy not doing that.",
"How do you spell no?",
"Sadly, I only have one body.",
"Sorry, but I no longer do things that make me want to kill myself.",
"Do fishes fly?",
"Ask me again in a few years.",
"Is nine plus ten equal to twenty one?",
"How does ‘no’ sound to you?",
"It sound like you’re looking for something that I’m not able to do right now.",
"I’m way too smart to say ‘yes’ to that.",
"What’s the opposite of positive?",
"My middle fingers are standing in salute.",
"Is the sky green?",
"Sorry, I don’t do that on days that end in Y.",
"There’s a person out there somewhere who’s a perfect fit for what you want. I am not that person.",
"No thanks, I’m a good person.",
"Is water dry?",
"You should do it yourself. You would be more awesome that way.",
"Give a moment. I’m trying to see how long I can go without saying yes.",
"How does ‘never’ work for you?",
"Is the sun cold?",
"No, I’m staying home to work on my booger structure.",
"Would you take ‘no’ for an answer?",
"Over my dead body!",
"Ewwww...no!",
"Not in this lifetime!",
"You deserve a ‘boo’ for that idea.",
"I’d rather be dead.",
"I’ve got too much on my plate right now.",
"Get lost, jerk!",
"You do know I hate you, right?",
"I’d rather stick several needles in my eyes. Or your eyes.",
"Not in a hundred years!",
"Not in a million years!",
"Not in a billion years!",
"Let’s just pretend that we don’t know each other.",
"The frown on my face says it all.",
"Which of the following is the funniest way to say 'no' for you?",
"That idea is bad, and you should be punished!",
"I’d rather sell my kidney.",
"Die!",
"Blah blah blah!",
"Drats! I would have loved to.",
"I’d rather eviscerate myself with a toothpick.",
"Umm...no thanks, loser!",
"I know a person who’s a better fit for that. I’ll email you their details.",
"Bah hambug!",
"Begone!"]

yn = random.randint(0,len(yes_no))
def yes_or_no():
    return yes_no[yn]