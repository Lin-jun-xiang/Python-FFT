# Fourier-Transform
* Visualize and analyze the fourier transform result.
* Final project

### Introduction

* 用 Python 實現傅立葉正(逆)轉換，並可視化結果。
* 傅立葉轉換目的 :了解原始訊號是由哪些頻率的cos,sin組成，將時域訊號轉換成頻域訊號觀看 (不同角度觀看數據)。
  * 濾波處理 : 當時域訊號非常雜亂複雜時，可以先進行正轉換取得頻域訊號，並針對感興趣的部分篩選，例如: 留下分量大的訊號，將分量小的頻號排除，再進行反轉換為時域訊號。

<p align="center">
<image SRC="https://user-images.githubusercontent.com/63782903/178134956-92ebace4-87ab-49cf-95be-2b5e27294c23.png" width=50%/>
</p>

* 每個訊號都是sin, cos以不同頻率組成，因此FT轉換目的是要得知訊號由哪些頻率的sin, cos組成。

* FT轉換後，大致上會得到實部 (cos) 跟虛部 (sin)，因此做圖因該分為實部與虛部來畫。

* 如果signal裡面只含有cos訊號，則得到的FT頻域應當只含有實部，這也是在積分項`evev(cos)*odd(sin)`會為0的原因。


### Method

例子 - 時域訊號及頻域解析解如下:
<p align="center">
<image src="https://user-images.githubusercontent.com/63782903/178135616-c7633824-f789-456a-ae71-28b9a9242565.png" width=50%/>


正轉換與逆轉換流程如下 (h為時域訊號；H為頻域訊號) :

<p align="center">
<image src="https://user-images.githubusercontent.com/63782903/178134447-04ee0eb7-9d92-4fac-8e15-51f91a8db4b2.png" width=50%/>


### Results

針對時域訊號進行不同採樣數量 (N=16, N=32, N=128)，並以不同採樣數量得數據進行正轉換，結果如下 :
(時域訊號中的紅色點，為採樣點)

可以發現 N=16 的轉換結果較為不同 (與解析解不同)，主要是採樣點不足 (dt > 0.5) 導致 **映頻效應(Aliasing)**

<p align="center">
<image SRC="https://user-images.githubusercontent.com/63782903/178135213-1c4f6f25-38da-4927-a7b3-9d600c20efab.png" WIDTH=50%/>

<p align="center">
<image src="https://user-images.githubusercontent.com/63782903/178135316-912ea526-c3fa-48e5-866f-b0be944456da.png" width=50%/>

逆轉換結果如下 : 
<p align="center">
<image SRC="https://user-images.githubusercontent.com/63782903/178135427-0f64184a-33e1-4411-b0ae-375295f5b477.png" WIDTH=50%/>

### Conclusion

* 採樣頻率(fs)需大於等於訊號最大頻率的2倍，才能建立完整訊號
* fs = 1/dt = N/T
* 例子中的訊號其最大頻率為 1，因此 fs 需大於等於 24
* 當 N = 16 時，不滿足條件，因此發生映頻效應
* fs 太小將無法抓取高頻訊號 ! 會將高頻訊號誤認為低頻訊號






