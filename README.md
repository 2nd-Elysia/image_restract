# image_restract

## 操作流程

1. 在transform中得到图1对图2的transform。
2. 对transform1to2和图2进行语义分割标记mask区域。（使用参考semantic里面的readme）
3. 对上面两张图的mask用mask_move来得到实际mask。
4. 在picture_add里面通过对mask区域去除互补相加得到不含条纹的background。
5. 在picture_minus_numpy中用图2减去background得到结果。

## 注意事项

- 图像路径更改。
- 可用picture_minus_cv2输出图像来判断背景匹配结果的正确性。