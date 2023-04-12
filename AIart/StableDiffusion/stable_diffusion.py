from datetime import datetime
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

#使用するモデルを設定
model_id = "stabilityai/stable-diffusion-2"

#StableDiffusionパイプライン設定
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16)

#使用する計算機を設定（GPUがない場合は"cpu"に変更）
pipe = pipe.to("cuda")

#画像生成の指示（呪文）
prompt = "a photo of an astronaut riding a horse on mars"

#描画する回数を設定
num_images = 2

#イラスト生成
for i in range(num_images):
  #推論実行
  image = pipe(prompt, height=768, width=768).images[0]

  #生成日時をファイル名にして保存
  date = datetime.now().strftime("%Y%m%d_%H%M%S")
  path = date + ".png"
  image.save(path)