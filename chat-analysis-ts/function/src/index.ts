import { Request, Response } from '@google-cloud/functions-framework';

export const processMessage = async (req: Request, res: Response) => {
  try {
    // 最小限の実装として、リクエストの内容をログに出力
    console.log('Received request:', req.body);

    // 成功レスポンスを返す
    res.status(200).send('Function executed successfully');
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
};
