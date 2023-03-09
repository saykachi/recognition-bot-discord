# recognition-bot-discord
This bot recognizes swear words in Russian and kicks the interlocutor out of the voice chat


Explanation:

First, we import the necessary modules, including discord for the Discord API, commands for creating bot commands, and speech_recognition for speech recognition.

We define the list of Russian swear words that we want to filter.

We create an instance of the Bot class and define the command prefix.

We define an on_ready event handler that is called when the bot is ready and prints a message to the console.

We define an on_voice_state_update event handler that is called when a user joins or leaves a voice channel. If the user joins the specified voice channel, the bot connects to the channel and starts listening to the audio stream.

We use the speech_recognition module to convert the audio stream to text. We then check if any of the Russian swear words are in the text, and if so, we disconnect the bot from the voice channel, wait for a second, and then reconnect to the channel.

Finally, we start the bot by calling client.run() with your Discord bot token.

**Note: This code is a simple example of how to filter swear words in Russian using speech recognition. It is not perfect and may have limitations. Also, make sure to replace <voice_channel_id> and <your_bot_token> with the appropriate values.**



by minirt/aisotoru
