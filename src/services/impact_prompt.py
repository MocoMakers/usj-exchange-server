import openai
openai.api_key = "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"

def impact_estimator(description):
    prompt = "Here is a product description: " + description + " Please tell me what this item is, and what it is made out of. Estimate how many are there, what the carbon footprint is, how much it weighs, and landfill breakdown by component. Please respond in json in the following format: \nitemName: \nitemMaterials: []\nquantity:\ncarbonFootPrint:\nitemWeight:\nlandfillBreakdown: []"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response