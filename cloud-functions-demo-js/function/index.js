// Google Cloud Storageクライアントライブラリをインポート
const {Storage} = require('@google-cloud/storage');

/**
 * GCSからファイルを読み取るHTTP Cloud Function
 *
 * 環境変数:
 * - BUCKET_NAME: 読み取るファイルが格納されているバケット名
 * - FILE_NAME: 読み取るファイル名（デフォルト: sample.txt）
 *
 * @param {Object} req Cloud Functionのリクエストコンテキスト
 * @param {Object} res Cloud Functionのレスポンスコンテキスト
 */
exports.helloWorld = async (req, res) => {
  // 環境変数からバケット名とファイル名を取得
  const bucketName = process.env.BUCKET_NAME;
  const fileName = process.env.FILE_NAME || 'sample.txt';

  console.log(`Start reading file: ${fileName} from bucket: ${bucketName}`);

  try {
    // GCSクライアントの初期化
    const storage = new Storage();
    // 指定されたバケットを取得
    const bucket = storage.bucket(bucketName);
    // 指定されたファイルを取得
    const file = bucket.file(fileName);

    // ファイルの内容をダウンロード
    const [content] = await file.download();
    console.log(`File content: ${content.toString()}`);

    // 成功レスポンスを返す
    res.status(200).send(content.toString());
  } catch (error) {
    // エラーが発生した場合はログに記録し、エラーレスポンスを返す
    console.error('Error:', error);
    res.status(500).send(error.message);
  }
};
