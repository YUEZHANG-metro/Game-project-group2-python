const webpack = require("webpack");

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: "export",

  webpack: (config, { isServer }) => {
    // 原有的 Cesium 配置
    config.plugins.push(
      new webpack.DefinePlugin({
        CESIUM_BASE_URL: JSON.stringify("cesium"),
      })
    );

    if (!isServer) {
      // 强制解析 zip.js 路径
      config.resolve.alias = {
        ...config.resolve.alias,
        '@zip.js/zip.js/lib/zip-no-worker.js': require.resolve('@zip.js/zip.js'),
        '@zip.js/zip.js/lib/zip-no-worker-inflate.js': require.resolve('@zip.js/zip.js'),
        '@zip.js/zip.js/lib/zip-no-worker-deflate.js': require.resolve('@zip.js/zip.js'),
      };

      config.resolve.fallback = {
        ...config.resolve.fallback,
        fs: false,
        http: false,
        https: false,
        zlib: false,
        url: false,
      };
    }

    return config;
  },

  experimental: {
    optimizePackageImports: ["@chakra-ui/react", "@mui"],
  },

  eslint: {
    ignoreDuringBuilds: true,
  },
};

module.exports = nextConfig;