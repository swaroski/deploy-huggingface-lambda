"""After executing this script, the model and tokenizer will be saved in the ./lambda/model directory. 
These will be bundled with your Docker image later on. This way, during Lambda invocations, 
the model and tokenizer are directly loaded from this directory, which is faster than fetching from 
the Hugging Face model hub.
"""


from transformers import AutoTokenizer, AutoModelForSequenceClassification

def get_model(model):
  """Loads model from Hugginface model hub"""
  try:
    model = AutoModelForSequenceClassification.from_pretrained(model)
    model.save_pretrained('./model')
  except Exception as e:
    raise(e)

def get_tokenizer(tokenizer):
  """Loads tokenizer from Hugginface model hub"""
  try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer)
    tokenizer.save_pretrained('./model')
  except Exception as e:
    raise(e)

get_tokenizer("cambridgeltl/sst_mobilebert-uncased")
get_model("cambridgeltl/sst_mobilebert-uncased")