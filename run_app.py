from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from ga_connector import GoogleConnector
from rasa_core.utils import EndpointConfig


action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/google_voice_nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint=action_endpoint)

input_channel = GoogleConnector()
print("run_app:")
agent.handle_channels([input_channel], 5004, serve_forever=True)