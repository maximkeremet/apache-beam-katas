import apache_beam as beam

inputs = ["Hello Beam"]

with beam.Pipeline() as pipeline:
    outputs = pipeline | "Say hello" >> beam.Create(inputs)
    outputs | beam.Map(print)
