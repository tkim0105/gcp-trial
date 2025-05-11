import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";
import * as fs from "fs";
import * as path from "path";

// プロジェクト設定の取得
const config = new pulumi.Config();
const project = config.require("project");

// Cloud Functions用のバケットを作成
const bucket = new gcp.storage.Bucket("chat-function-bucket", {
    location: "asia-northeast1",
    project: project,
});

// 関数のソースコードをアップロード
const functionZip = new gcp.storage.BucketObject("function.zip", {
    bucket: bucket.name,
    source: new pulumi.asset.FileAsset(path.join(__dirname, "function", "function.zip")),
});

// Cloud Functionsのデプロイ
const cloudFunction = new gcp.cloudfunctions.Function("chat-function", {
    project: project,
    region: "asia-northeast1",
    runtime: "nodejs18",
    sourceArchiveBucket: bucket.name,
    sourceArchiveObject: functionZip.name,
    entryPoint: "processMessage",
    triggerHttp: true,
    availableMemoryMb: 256,
    environmentVariables: {
        NODE_ENV: "production",
    },
});

// Cloud Functionsの公開アクセスを許可
const invoker = new gcp.cloudfunctions.FunctionIamMember("function-invoker", {
    project: project,
    region: "asia-northeast1",
    cloudFunction: cloudFunction.name,
    role: "roles/cloudfunctions.invoker",
    member: "allUsers",
});

// 関数のURLを出力
export const functionUrl = cloudFunction.httpsTriggerUrl;
