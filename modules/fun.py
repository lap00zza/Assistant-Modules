from assistant import command


class FunCommands:
    def __init__(self, assistant):
        self.assistant = assistant

    @command(description="A sample command to demonstrate modules.")
    async def test_state(self, message):
        await self.assistant.send_message(message.channel, "This is from a downloaded module.")


def load(assistant):
    assistant.add_module(FunCommands(assistant))
